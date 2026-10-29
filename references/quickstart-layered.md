# 安装依赖与复跑样片

先安装整个 Skill 文件夹，保持 SKILL.md、scripts、assets、examples、references 与许可证的相对位置。下面命令均在这个文件夹中执行。

## 1. 准备依赖

使用现有 Python、Node 和 FFmpeg，缺少时通过它们的官方渠道安装。Python 库与 Node 依赖可放在项目局部，避免影响其他工程：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm install --prefix .runtime hyperframes@0.8.183 gsap@3.15.0
```

macOS/Linux 对应的 Python 为 `.venv/bin/python`。Node 可用 `Get-Command node`（PowerShell）或 `command -v node`（macOS/Linux）定位。HyperFrames 入口为 `.runtime/node_modules/hyperframes/bin/hyperframes.mjs`，GSAP 为 `.runtime/node_modules/gsap/dist/gsap.min.js`。

FFmpeg 与 FFprobe 应在同一目录。命令中的 `FFmpeg路径` 换成实际完整路径。系统应安装 Microsoft YaHei、Noto Sans CJK SC 等中文字体；先检查短样的汉字，没有字体时先补齐。首次 HyperFrames 渲染可能需要下载浏览器运行依赖，应根据工具的实际提示处理。

## 2. 在新目录准备项目

复制 `examples/work-focus-layered` 到自己的项目目录，保留 story.json 与 character-puppet.png 的相对位置。先用原配置跑通，再修改标题和旁文。

给 WorkBuddy 的分镜提示词：

> 用 paper-collage-workbuddy，把“忙了一整天，正事没动；一被打断，就要重来；先完成最重要的那件”拆成三个分镜。用表格列出表达目的、独立动作和画面结果。保留人物、纸张、消息与时钟分层运动，沿用橙绿奶油白。先出分镜，不渲染。

确认后再输入：

> 读取本期 story.json，按 render_lifestyle_layers.py 的真实参数实际渲染。三段各4秒，1280×720、60fps，动作结束停稳。生成 warm-focus 器乐并混入最终MP4。使用新输出文件名，保留可编辑工程、独立配乐和运行报告，打开最终成片。不要复制已有视频代替渲染。

## 3. 实际运行命令

Windows PowerShell：

```powershell
$nodePath = (Get-Command node).Source
.\.venv\Scripts\python.exe scripts/render_lifestyle_layers.py examples/work-focus-layered/story.json output/my-first-video.mp4 --node "$nodePath" --hyperframes .runtime/node_modules/hyperframes/bin/hyperframes.mjs --gsap .runtime/node_modules/gsap/dist/gsap.min.js --ffmpeg "FFmpeg路径"
```

macOS/Linux：

```bash
.venv/bin/python scripts/render_lifestyle_layers.py examples/work-focus-layered/story.json output/my-first-video.mp4 --node "$(command -v node)" --hyperframes .runtime/node_modules/hyperframes/bin/hyperframes.mjs --gsap .runtime/node_modules/gsap/dist/gsap.min.js --ffmpeg "FFmpeg路径"
```

每次使用不同文件名。`--build-only` 仅构建可编辑 HTML；需去掉该参数才能得到视频。当前构图是三段各至少4秒、1280×720。新画幅或其他叙事先修改模板和编舞，不直接截断动作。

## 4. 检查交付

最终文件为指定输出 MP4。旁边的 `成片-assets` 保存 editable、story.json、bgm-original.wav 和 render-report.json。不要交付无配乐的 picture.mp4 中间件。

看动作是否连贯、结束是否停稳、文字有无方框，听音乐是否完整及人声是否清楚。抽帧、机器识别和技术数值与完整观看、实际听审分开记录。


## 使用完整工作流

新选题先读 SKILL.md 与 workbuddy-workflow.md。先运行 `python scripts/workflow.py plan 本期/beats.json 新计划目录` 导出分镜、素材提示词和动作计划；准备真实素材与 HTML 后运行 workflow.py render。完整字段见 project-schema.md。随包样片也可经 workflow.py render examples/work-focus-layered/beats.json 新版本.mp4，后接相同的四个依赖路径参数。
