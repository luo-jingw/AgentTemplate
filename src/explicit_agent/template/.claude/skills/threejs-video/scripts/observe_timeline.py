"""Read a video timeline and emit measurements without modifying any input."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, field
import hashlib
import json
import math
from pathlib import Path
import sys


@dataclass(frozen=True)
class Finding:
    location: str
    kind: str
    detail: str


@dataclass(frozen=True)
class Interval:
    index: int
    start: float
    end: float


@dataclass
class TimelineObservation:
    input_path: str
    input_sha256: str = ""
    language: str | None = None
    duration_seconds: float | None = None
    chapter_count: int = 0
    caption_count: int = 0
    valid_chapter_intervals: int = 0
    valid_caption_intervals: int = 0
    translated_caption_count: int = 0
    caption_duration_min_seconds: float | None = None
    caption_duration_max_seconds: float | None = None
    chapter_end_minus_duration_seconds: float | None = None
    caption_end_minus_duration_seconds: float | None = None
    numerical_tolerance_seconds: float = 1e-6
    findings: list[Finding] = field(default_factory=list)
    read_error: str | None = None


class TimelineObserver:
    """Own one report; structural observations are separate from acceptance."""

    def __init__(self, path: Path, require_translation: bool) -> None:
        self.path = path.resolve()
        self.require_translation = require_translation
        self.report = TimelineObservation(str(self.path))

    def note(self, location: str, kind: str, detail: str) -> None:
        self.report.findings.append(Finding(location, kind, detail))

    @staticmethod
    def finite_number(value: object) -> float | None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return None
        try:
            number = float(value)
        except OverflowError:
            return None
        return number if math.isfinite(number) else None

    def intervals(self, raw: object, name: str) -> list[Interval]:
        if not isinstance(raw, list):
            self.note(name, "not_array", "Expected an array")
            return []
        if not raw:
            self.note(name, "empty_array", "No entries")
        intervals: list[Interval] = []
        chapter_ids: list[str] = []
        for index, item in enumerate(raw):
            location = f"{name}[{index}]"
            if not isinstance(item, dict):
                self.note(location, "not_object", "Expected a JSON object")
                continue
            if name == "chapters":
                chapter_id = item.get("id")
                if isinstance(chapter_id, str) and chapter_id.strip():
                    chapter_ids.append(chapter_id)
                else:
                    self.note(location, "missing_chapter_id", "id must be nonempty text")
            else:
                text = item.get("text")
                if not isinstance(text, str) or not text.strip():
                    self.note(location, "missing_caption_text", "text must be nonempty")
                translation = item.get("translation")
                if isinstance(translation, str) and translation.strip():
                    self.report.translated_caption_count += 1
                elif self.require_translation:
                    self.note(location, "missing_translation", "Translation requested")
            start = self.finite_number(item.get("start"))
            end = self.finite_number(item.get("end"))
            if start is None or end is None:
                self.note(location, "invalid_time", "start/end must be finite numbers")
                continue
            if end <= start:
                self.note(location, "nonpositive_duration", f"end-start={end - start}")
                continue
            tolerance = self.report.numerical_tolerance_seconds
            if start < -tolerance:
                self.note(location, "negative_start", f"start={start}")
            duration = self.report.duration_seconds
            if duration is not None and end > duration + tolerance:
                self.note(location, "beyond_duration", f"end-duration={end - duration}")
            intervals.append(Interval(index, start, end))
        for chapter_id, count in Counter(chapter_ids).items():
            if count > 1:
                self.note("chapters", "duplicate_chapter_id", f"{chapter_id}: {count}")
        previous_start = -math.inf
        furthest_end = -math.inf
        for span in intervals:
            location = f"{name}[{span.index}]"
            if span.start < previous_start:
                self.note(location, "out_of_order", f"start={span.start}")
            if span.start < furthest_end - self.report.numerical_tolerance_seconds:
                self.note(location, "overlap", f"overlap_seconds={furthest_end - span.start}; previous coverage end={furthest_end}")
            previous_start = span.start
            furthest_end = max(furthest_end, span.end)
        return intervals

    def observe(self) -> TimelineObservation:
        try:
            raw = self.path.read_bytes()
            self.report.input_sha256 = hashlib.sha256(raw).hexdigest()
            data: object = json.loads(raw.decode("utf-8-sig"))
        except (OSError, UnicodeError, ValueError) as error:
            self.report.read_error = str(error)
            return self.report
        if not isinstance(data, dict):
            self.note("root", "not_object", "Expected a JSON object")
            return self.report
        language = data.get("language")
        if isinstance(language, str) and language.strip():
            self.report.language = language
        else:
            self.note("language", "missing_language", "Expected nonempty text")
        duration = self.finite_number(data.get("duration"))
        if duration is None or duration <= 0:
            self.note("duration", "invalid_duration", "Expected positive finite seconds")
        else:
            self.report.duration_seconds = duration
        chapters_raw = data.get("chapters")
        captions_raw = data.get("captions")
        self.report.chapter_count = len(chapters_raw) if isinstance(chapters_raw, list) else 0
        self.report.caption_count = len(captions_raw) if isinstance(captions_raw, list) else 0
        chapters = self.intervals(chapters_raw, "chapters")
        captions = self.intervals(captions_raw, "captions")
        self.report.valid_chapter_intervals = len(chapters)
        self.report.valid_caption_intervals = len(captions)
        if captions:
            lengths = [span.end - span.start for span in captions]
            self.report.caption_duration_min_seconds = min(lengths)
            self.report.caption_duration_max_seconds = max(lengths)
        if self.report.duration_seconds is not None:
            if chapters:
                self.report.chapter_end_minus_duration_seconds = max(s.end for s in chapters) - self.report.duration_seconds
            if captions:
                self.report.caption_end_minus_duration_seconds = max(s.end for s in captions) - self.report.duration_seconds
        tolerance = self.report.numerical_tolerance_seconds
        for caption in captions:
            owners = [chapter.index for chapter in chapters
                      if chapter.start - tolerance <= caption.start
                      and caption.end <= chapter.end + tolerance]
            if len(owners) != 1:
                self.note(f"captions[{caption.index}]", "chapter_containment_count",
                          f"Containing chapters: {owners}")
        return self.report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeline", type=Path, required=True)
    parser.add_argument("--require-translation", action="store_true")
    arguments = parser.parse_args()
    report = TimelineObserver(arguments.timeline, arguments.require_translation).observe()
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(asdict(report), ensure_ascii=False, indent=2, allow_nan=False))
    return 2 if report.read_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
