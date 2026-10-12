# 代码骨架（HTML 内联 SVG，自动适配深浅色）

```html
<style>
:root{--fg:#1f1e1b;--muted:#6b6a64;--card:#fff;--line:#dedcd3;
  --box-f:#fff;--box-s:#b4b2a9;
  --gray-f:#F1EFE8;--gray-s:#888780;--gray-t:#444441;--gray-t2:#5F5E5A;
  --teal-f:#E1F5EE;--teal-s:#0F6E56;--teal-t:#085041;--teal-t2:#0F6E56;
  --purple-f:#EEEDFE;--purple-s:#534AB7;--purple-t:#3C3489;--purple-t2:#534AB7;
  --coral-f:#FAECE7;--coral-s:#993C1D;--coral-t:#712B13;--coral-t2:#993C1D}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--fg:#ecebe6;--muted:#a3a29b;--card:#232321;--line:#3a3936;
  --box-f:#232321;--box-s:#5F5E5A;
  --gray-f:#444441;--gray-s:#B4B2A9;--gray-t:#F1EFE8;--gray-t2:#D3D1C7;
  --teal-f:#085041;--teal-s:#5DCAA5;--teal-t:#E1F5EE;--teal-t2:#9FE1CB;
  --purple-f:#3C3489;--purple-s:#AFA9EC;--purple-t:#EEEDFE;--purple-t2:#CECBF6;
  --coral-f:#712B13;--coral-s:#F0997B;--coral-t:#FAECE7;--coral-t2:#F5C4B3}}
:root[data-theme="dark"]{--fg:#ecebe6;--muted:#a3a29b;--card:#232321;--line:#3a3936;
  --box-f:#232321;--box-s:#5F5E5A;
  --gray-f:#444441;--gray-s:#B4B2A9;--gray-t:#F1EFE8;--gray-t2:#D3D1C7;
  --teal-f:#085041;--teal-s:#5DCAA5;--teal-t:#E1F5EE;--teal-t2:#9FE1CB;
  --purple-f:#3C3489;--purple-s:#AFA9EC;--purple-t:#EEEDFE;--purple-t2:#CECBF6;
  --coral-f:#712B13;--coral-s:#F0997B;--coral-t:#FAECE7;--coral-t2:#F5C4B3}
figure{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:20px 0}
figure svg{width:100%;height:auto;display:block}
figcaption{font-size:13px;color:var(--muted);margin-top:8px}
svg .th{font-size:14px;font-weight:600;fill:var(--fg)}
svg .t{font-size:14px;fill:var(--fg)}
svg .ts{font-size:12px;fill:var(--muted)}
svg rect{stroke-width:.7}
svg .g-box rect{fill:var(--box-f);stroke:var(--box-s)}
svg .g-gray rect{fill:var(--gray-f);stroke:var(--gray-s)} svg .g-gray .th{fill:var(--gray-t)} svg .g-gray .ts{fill:var(--gray-t2)}
svg .g-teal rect{fill:var(--teal-f);stroke:var(--teal-s)} svg .g-teal .th{fill:var(--teal-t)} svg .g-teal .ts{fill:var(--teal-t2)}
svg .g-purple rect{fill:var(--purple-f);stroke:var(--purple-s)} svg .g-purple .th{fill:var(--purple-t)} svg .g-purple .ts{fill:var(--purple-t2)}
svg .g-coral rect{fill:var(--coral-f);stroke:var(--coral-s)} svg .g-coral .th{fill:var(--coral-t)} svg .g-coral .ts{fill:var(--coral-t2)}
svg .dashed rect,svg .masked{fill:none;stroke:var(--box-s);stroke-dasharray:3 3}
svg .arr{stroke:var(--muted);stroke-width:1.2;fill:none}
</style>

<!-- 全文共用的箭头定义，只放一次 -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" style="stroke:var(--muted)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</marker></defs></svg>

<figure>
<svg viewBox="0 0 680 220" role="img" aria-label="示例">
  <!-- 中性双行框 -->
  <g class="g-box"><rect x="260" y="30" width="160" height="56" rx="8"/></g>
  <text class="th" x="340" y="49" text-anchor="middle" dominant-baseline="central">输入</text>
  <text class="ts" x="340" y="68" text-anchor="middle" dominant-baseline="central">B × L × 3072</text>
  <!-- 直线箭头 -->
  <line class="arr" x1="340" y1="86" x2="340" y2="117" marker-end="url(#arrow)"/>
  <!-- 彩色双行框：rect 和 text 都放在同一个 g 里，文字才会变色 -->
  <g class="g-purple">
    <rect x="180" y="120" width="320" height="56" rx="8"/>
    <text class="th" x="340" y="139" text-anchor="middle" dominant-baseline="central">共享主干 ×28</text>
    <text class="ts" x="340" y="158" text-anchor="middle" dominant-baseline="central">全双向注意力</text>
  </g>
  <text class="ts" x="340" y="204" text-anchor="middle">紫：共享主干</text>
</svg>
<figcaption>图 1　一句话说明这张图回答的问题，以及读图要点。</figcaption>
</figure>
```

要点：彩色框的 `<rect>` 和框内 `<text>` 必须是同一个 `<g class="g-xxx">` 的子元素；中性框的文字可以放在 `g` 外面。

深浅色除了跟随系统的 `prefers-color-scheme`，还响应显式的 `[data-theme="dark"/"light"]`（发布为 Artifact 等场景会由宿主在根元素上显式打这个属性，覆盖系统偏好）；两套规则共用同一组色值，不要只改一处。

## 图注与正文

- 每张图用 `<figure>` 包裹，下方必须有 `<figcaption>`：以"图 N"开头，一句话说清这张图回答什么问题，必要时补充读图方法或数字出处。
- 图前用一两句话引出这张图要看什么，图后用正文或表格补充图里放不下的细节。
- 精确的超参、维度、配比放在表格里，不要硬塞进图中。
- 如果某个数字在不同来源里不一致，在正文或备注中注明，不要在图里自行取舍而不说明。
