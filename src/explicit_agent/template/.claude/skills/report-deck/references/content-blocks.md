# 内容组件

每种组件对应一类问题；选错组件比选错配色更容易误导读者，先想清楚要表达什么关系，再挑组件。

## 统计块（`.stats`）

```html
<div class="stats">
  <div><span class="big">93.4</span><span>主指标名称<br>对照基线 91.8</span></div>
</div>
```

用于"一两个关键数字，读者应该先看到它们"。`big` 只放数字本身；对照值、单位、口径放进后面的 `<span>`，可以用 `<br>` 换行成两行小字。不要把统计块当表格用——超过 3-4 个数字就该用表格。

## 状态徽章（`.pill`）

```html
<span class="pill ok">是</span>
<span class="pill nc">非商用许可</span>
<span class="pill no">闭源</span>
<span class="pill mid">—</span>
```

四种状态的含义固定，不要挪作他用：

| class | 含义 | 不是 |
|---|---|---|
| `ok` | 已确认 / 可复现 / 满足条件 | "效果好" |
| `nc` | 有条件（部分满足、需要额外步骤、许可受限） | "一般" |
| `no` | 无法验证、未知、不满足 | "效果差" |
| `mid` | 中性、不适用、未测 | "及格" |

徽章回答的是"这件事能不能被验证"，不是"这件事好不好"——效果好坏应该用具体数字说话，不要用颜色代替。

## 表格（`.tw > table`）

```html
<div class="tw"><table>
<thead><tr><th>名称</th><th>来源</th><th class="num">指标</th><th>状态</th></tr></thead>
<tbody>
<tr><td class="name">方法 A<span class="org">机构 X</span></td><td class="refs">论文/链接</td><td class="num mono">12.3</td><td><span class="pill ok">是</span></td></tr>
</tbody>
</table></div>
```

- `.tw` 包一层处理横向溢出（窄屏自动出现横向滚动条）。
- `td.name` 加粗，配 `span.org` 放次要的机构/来源小字。
- 数字列用 `class="num mono"`：右对齐、等宽字体，方便竖着比大小。
- `td.refs`、`td.date` 用 `white-space:nowrap`，避免引用标识或日期被意外折行拆散。

## 定义列表（`dl.kv`）

```html
<dl class="kv">
  <dt>评测方式</dt><dd>怎么测的，样本量多少</dd>
  <dt>已知限制</dt><dd>一句话说清不能外推到什么场景</dd>
</dl>
```

用于"若干个标签-说明对"，比如方法论细节、已知限制、评测口径——内容不是表格那种多行可比较的数据，而是每条单独成立的说明。

## 训练/任务进度卡片（`.runs > .run`）

```html
<div class="runs">
  <div class="run s-a">
    <div class="run-h"><b>名称</b><span class="pct">47.5%</span></div>
    <div class="bar"><b style="--w:47.5%"></b></div>
    <p><span class="mono">33,190 / 69,900</span> 步 · 硬件配置 · 速度与稳定性</p>
    <p>预计 <b class="mono">01-05 18:00</b> 完成</p>
  </div>
</div>
```

`s-a`/`s-b`/`s-c` 这几个系列 class 同时控制卡片的进度条颜色和对应曲线图里那条线的颜色——同一个 run 在卡片和图表里应该用同一个系列 class，读者靠颜色就能把两处对应起来，不要在卡片和图表里给同一个 run 用不同颜色。

百分比、步数、预计完成时间都要是当次写报告时的真实值，不要用占位符交付；`<b class="mono">`包裹的时间戳要能在旁边的曲线图里找到对应的点。

## 大列表（`.big-list`）

用于"开放问题"、"下一步计划"这类条目独立、需要稍大字号强调的列表，和普通 `<ul>`（用于次要说明）区分开。不要在一页里同时放两种列表让读者分不清主次。
