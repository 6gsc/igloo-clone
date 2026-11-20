# 改字防乱码规范（血泪经验版）

> 本站不是普通网页，文字分两条渲染管线。改字前先分清你改的是哪条线，再按对应流程操作。
> 本文档由实际踩坑总结，每条规则背后都是一次真实的乱码事故。

---

## 一、先搞清楚：你要改的字在哪条线

| 线 | 渲染方式 | 涉及文件 | 改字难度 |
|---|---|---|---|
| **A. 3D 场景文字**（宣言、版权、滚动提示、项目卡标题/摘要、Sound/On/Off、TEMP、日期、CLICK TO EXPLORE） | MSDF 字体图集，逐字拼形 | `assets/App3D-d68cb154.js` 里的字符串 + `assets/fonts/` 两个字库文件 | 中（改完必须重建字库） |
| **B. UI 图标/logo**（左上角 Gui、声音图标、关闭叉、箭头） | 独立位图纹理，整图贴一个面 | `assets/images/ui/*-datatexture.ktx2` | 高（要重做纹理） |
| **C. 浏览器标签页/分享卡片** | 普通 HTML | `index.html` 的 title/meta | 零（直接改，中文随便用） |

**判断方法**：在 `assets/App3D-d68cb154.js` 里搜你要改的文字——
- 搜得到 → A 线，走第二节流程
- 搜不到、是图标/logo → B 线，走第五节
- 标签页标题 → C 线，改 `index.html`

---

## 二、A 线标准流程（改 3D 场景文字）

```bash
# 第 1 步：改文案
# 编辑 assets/App3D-d68cb154.js，搜索旧文案直接替换。
# 注意：引号结构别动（"..." 或 `...`），模板串 `...` 里可以换行

# 第 2 步：重建字库（必跑！新字不在库里就是空格）
cd igloo-clone
./rebuild_font.sh

# 第 3 步：刷新浏览器（普通刷新即可，服务器已是 no-cache）
```

### rebuild_font.sh 做了什么（出问题时按此排查）

1. 扫描 bundle 里**全部字符串字面量**，收集所有用到的字符
2. 合并字体：拉丁/数字用 IBM Plex Mono（**锁死原版等宽 metrics**），中文从 Arial Unicode 按比例缩放并入
3. msdf-atlas-gen 生成图集（size 42 / pxrange 4，与原版一致）
4. toktx 编码成 UASTC KTX2（带 `--lower_left_maps_to_s0t0` 行序翻转）
5. 替换 `assets/fonts/IBMPlexMono-Medium.json` + `IBMPlexMono-Medium-datatexture.ktx2`

前置依赖：`pip3 install fonttools brotly`（工具本体已内置 tools/ 目录，离线可用）

---

## 三、三大乱码坑（A 线）

每一格都是真实事故，改字前对照检查：

| # | 坑 | 屏幕症状 | 控制台信号 | 规则 |
|---|---|---|---|---|
| 1 | **字不在字库** | 该字变空格，文字缺笔画断开 | `X is not present in the MSDF font atlas` | 改了文案**必须**跑 rebuild_font.sh，跑完看控制台这条警告是不是 0 |
| 2 | **压缩格式错** | 整屏雪花/破碎噪点 | Texture load 报错 | 只能用 **UASTC**（`--encode uastc --uastc 4`）。ETC1S 会毁掉 MSDF 距离场；未压缩 KTX2 这版加载器不认 |
| 3 | **纹理行序颠倒** | 字形能显示但全是**错字碎片**（看着像加密电报） | 无报错，最隐蔽 | toktx 必须带 `--lower_left_maps_to_s0t0`。采样代码用 GL 风格纵坐标，png 默认行序是反的 |

**症状速查**：
- 字缺了/空格 → 坑 1
- 全屏花 → 坑 2
- 有字但不是那个字 → 坑 3
- 字对但位置叠了 → 看第四节布局耦合
- 改了没反应 → 浏览器缓存，确认服务器是 `nocache_server.py` 在跑

---

## 四、布局耦合警告（A 线进阶）

**拉丁字符的 metrics 不能变**。Sound/On/Off、TEMP、日期这些 UI 的坐标是按原版 IBM Plex Mono 的字宽（每字 0.6em）和字高（1.5em）写死的。换成比例宽度字体（如直接用中文字体渲染英文）→ **文字重叠**。

- `merge_font.py` 已保证拉丁用 Plex metrics，别绕过它自己拼字体
- Sound 面板偏移系数已补偿过：`size.y*t*5.2`（原 2.6，共 2 处）、`.783`（原 .45，3 处）——**因为新字库的字形高度框是 0.86em，原版是 1.5em**。如果你以后做了统一格子的字库，要改回 2.6/.45
- 中文行高比原版略宽（1.48 vs 1.3），多行中文更透气，属预期不是 bug

---

## 五、B 线：换 logo / 图标

**核心认知（两小时坑换来的）**：`ui/*-datatexture.ktx2` 这类纹理**不是 SDF/MSDF**，是普通位图——**白字(255) + 黑底(0)**，alpha 通道全 0 没用。给它 SDF 距离场数据会渲染成半透明糊片，怎么调都糊。

**正确做法**（已封装成脚本）：

```bash
python3 tools/fonts/make_logo.py "Gui"
# 然后把 assets/images/ui/logo-custom-datatexture.ktx2 重命名为正式文件名
# 再改 bundle 里的引用（搜 logo-datatexture）
```

三条铁律：
1. **字号 ≤ 40px**（128×128 纹理，字太大会被显示框压扁变形）
2. **文字必须铺满整个 128px 宽**——小视口（手机宽度）下 logo 纹理会被水平平铺采样（repeat），只画中间一小块会平铺出重叠错位。原版 IGLOO 就是 5 字母满铺设计。`make_logo.py` 逐字槽位排布已处理
3. **像素数据移植进原版容器**（保留 header/DFD 字节，只换数据段）——不要自己从零构造 KTX2
4. 换**新文件名** + 改 bundle 引用，绕过浏览器缓存

---

## 六、常用命令速查

```bash
./serve.sh                    # 起本地服务（no-cache 版）→ http://127.0.0.1:8791/
./rebuild_font.sh             # 重建中文字库（改完 A 线文案必跑）
./download.sh                 # 从官网重新镜像资源（原站更新后用）
python3 tools/fonts/make_logo.py "文字"   # 生成新 logo 纹理
```

**验证清单**（每次改字后过一遍）：

1. 浏览器 Console 搜 `not present` → 应为 0 条
2. 浏览器 Console 搜 `error` → 应为 0 条
3. 服务器日志 `grep ' 404 ' /tmp/igloo_nocache.log` → 应为空
4. 肉眼过一遍五个区域：左上 logo、版权区、宣言、左下滚动提示、项目卡

---

## 七、出事了怎么回滚

| 场景 | 操作 |
|---|---|
| JS 改坏了 | `cp assets/App3D-d68cb154.js.bak assets/App3D-d68cb154.js`（原版备份） |
| 字库想回到纯英文原版 | `curl -o assets/fonts/IBMPlexMono-Medium.json https://www.igloo.inc/assets/fonts/IBMPlexMono-Medium.json`（ktx2 同路径换文件名） |
| logo 想回 IGLOO | bundle 引用改回 `ui/logo-datatexture.ktx2`（原文件还在） |
| 全部重来 | `./download.sh` 重新镜像，再重跑中文化流程 |

---

## 附：本站文字渲染原理（想深入再看）

- **A 线**：`msdfworker` Web Worker 按 json 字形表逐字排版，每个字符一个四边形面片，UV 从 KTX2 图集取字形，shader `median(三通道)-0.5` 解码出字形 alpha。中英文混排天然支持，前提是字库里得有这个字
- **B 线**：整张贴图，位图亮度即透明度
- 为什么标签页能用中文而场景文字要重建字库：标签页是浏览器系统字体渲染；场景文字是 GPU 纹理采样，没有的字就是不存在
