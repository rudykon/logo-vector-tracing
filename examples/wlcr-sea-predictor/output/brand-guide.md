# WLCR-SEA Predictor Vector Master

本套文件以 `logo.png` 为构图母版重新分层描摹。图标、图表、字标均为 SVG 几何对象；不含 `<text>`、位图 `<image>` 或外部字体依赖。

## 文件用途

| 文件 | 用途 | 推荐场景 |
|---|---|---|
| `logo.svg` | 竖版主标，透明画布 | README、Hugging Face model card、文档封面 |
| `logo-icon.svg` | 800 × 800 App Icon | 应用图标、项目头像、社交账号 |
| `logo-horizontal.svg` | 1600 × 520 横版 | 网站页眉、文档横幅、演示文稿 |
| `logo-dark.svg` | 深色背景竖版 | 深色 README、夜间界面、视频片尾 |
| `favicon.svg` | 512 × 512 紧凑图标 | 浏览器 favicon、PWA、仓库小图标 |

## 视觉构成

- App Icon 使用 145/800 的连续圆角比例，保留天空渐变、双层海岸山丘和白色预测曲面。
- 通信塔由独立桁架路径构成；三组左右对称信号波纹均使用圆端 Bézier 曲线。
- 数据层包含 3 个观测节点、5 级半透明柱形、虚线预测轨迹、定制上升箭头和验证章。
- `WLCR-SEA` 与 `Predictor` 已从字体轮廓转换为 path；`SEA`、副标题和装饰线保留蓝绿渐变关系。

## 标准色

| 名称 | HEX | 用途 |
|---|---:|---|
| Signal Blue | `#0789F4` | 天空、SEA 字标、装饰线 |
| Sky Cyan | `#43D0EA` | 天空渐变末端 |
| Tower Navy | `#03265E` | 通信塔、主字标 |
| Ridge Teal | `#12B6A4` | 前景山丘 |
| Deep Teal | `#05999B` | 远近层次 |
| Forecast Teal | `#00A89E` | 折线、箭头、验证章 |
| Chart Blue | `#B9DCFF` | 半透明柱状图 |
| Night Navy | `#061A3B` | 深色版背景 |

## 留白与最小尺寸

主标四周至少保留图标宽度的 8% 作为安全区。竖版建议最小显示宽度 220 px，横版建议最小显示宽度 420 px，图标建议不小于 48 px。低于 32 px 时优先使用 `favicon.svg`，避免塔架与柱形细节变得拥挤。

## 平台使用

GitHub 与 Hugging Face 可直接引用 SVG；若平台对 SVG 有安全过滤，使用项目随附的 SVG 渲染预览导出 PNG。文档和演示中应保持原始宽高比，不拉伸、不重排元素、不替换字标字体。深色界面使用 `logo-dark.svg`；不要把普通版的深蓝字标直接放在深色背景上。

## 完整性检查

所有交付 SVG 均采用 `viewBox`，可无损缩放；渐变、透明度、圆角和 Bézier 曲线均保留。为保证跨平台一致性，不应将 path 重新转回可编辑文本。
