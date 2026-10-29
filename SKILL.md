---
name: paper-collage-workbuddy
description: 基于 Vox Director 改造的生活职场动画完整制作流程。由 WorkBuddy 从选题或文案组织分镜、风格、素材和独立动效，调用 HyperFrames、原创配乐与 FFmpeg，交付 MP4、可编辑工程和制作文档。
---

# 生活职场动画 · WorkBuddy 优化版

本 Skill 在 Vox Director 的“主题→叙事弧→beats/shots分镜→视觉与素材→元素动作→旁白/音乐→合成→核验”流程上改造。保留它的故事层、视觉层和风格提示词组合代码，执行默认改为 WorkBuddy 自身模型加本地 HyperFrames、GSAP 和 FFmpeg。具体继承文件和改动见 [二次开发说明](references/adaptation.md)。

## 先选执行入口

- **新选题或新文案**：按 [完整制作流程](references/workbuddy-workflow.md) 工作，使用上游 `beats`/`shots` 数据结构，先组织故事、分镜与动作，再准备素材和可编辑 HTML，最后调用 `scripts/workflow.py`。不同故事重新编舞，不能套用旧场景冒充新创作。
- **复跑已认可的橙绿样片**：使用 `examples/work-focus-layered/beats.json`，`renderer: focus-layered` 接通已实跑的三段人物动画。这只是随包成品案例，不能拿它限制新故事，也不能通过只换三个标题声称完成任意选题。
- **修画面**：保留已认可文案和音轨，只修改用户要求的素材、动作、构图或节奏，输出新版本。

## 完整流程

1. 明确观众、具体烦恼、叙事目的和一个有帮助的结果。用户已有定稿或选题时沿用；缺少关键素材可先列缺口，同时完成其他准备。
2. 参考 [上游故事层](references/upstream/beat-layer.md)，按主题选叙事弧。WorkBuddy 的当前真实可用模型负责写 `beats.json`：逐段正文、标题、场景、镜头时长、景别、运镜及各物件的独立动作。保留已认可文字，不依靠脚本假装调用大模型。
3. 参考 [上游视觉层](references/upstream/prompt-guide.md)，明确统一风格、配色、纸纹和人物一致性。本账号既定风格为橙、深青绿、奶油白，用户已认可时直接沿用。标题使用独立文字层，素材生成不烧标题。`workflow.py plan` 实际复用上游风格组合器，导出分镜、素材提示词和动作计划，详见 [项目参数](references/project-schema.md)。
4. 用 WorkBuddy 实际可用的图像工具、用户素材或有权使用的素材准备独立部件。没有图像能力时列出具体素材缺口及提示词，不假称生成成功，不把整幅静图平移算成物件动作。人物和道具需能独立运动，先验透明边缘与构图。
5. 根据每镜场景和 `element_motion` 生成/修改 HyperFrames 可编辑 HTML，不局限三段示例。固定主体与纸纹，人物、手臂、纸张、通知和道具按事件行动、结束停稳。标题稳定，不加入持续随机位移和无休止晃动。新故事的实际资产与动作都要落到工程，不能只停留在分镜表。
6. 默认生成完整原创器乐。保留已认可口播：若本项目指定剪映配音，沿用用户指定的原生流程；不擅换音色、变速变调或重新生成整稿。无口播就输出器乐样片，用户明确要求无声才用 none。音频参数见 [分层配置](references/layered-lifestyle.md)。
7. 执行 `workflow.py render`，实际渲染画面并混入音乐/口播，输出最终 MP4、可编辑工程、分镜与素材、独立配乐、运行报告。旁白长于画面时先延长分镜，脚本拒绝静默截断。不同画幅按实际构图制作，不拉伸或裁掉动作。
8. 检查最终 MP4 的文字、动作完成度、转场、音轨和口播完整性。技术检查、抽帧、连续观看、实际听审及用户认可分开记录。失败应修复本环节，不复制旧成片或用无声中间件交付。

## 命令与默认依赖

`python scripts/workflow.py check 项目/beats.json`

`python scripts/workflow.py plan 项目/beats.json 新的计划目录`

`python scripts/workflow.py render 项目/beats.json 新版本.mp4 --node Node路径 --hyperframes hyperframes.mjs路径 --gsap gsap.min.js路径 --ffmpeg FFmpeg路径`

使用 Python/Pillow/NumPy、Node、HyperFrames、GSAP 和同目录 FFmpeg/FFprobe。检查真实依赖路径和中文字体，安装说明见 [上手流程](references/quickstart-layered.md)。默认流程不要求 Atlas Cloud、MiniMax 或其他付费 API，也不声称已接入这些服务。

## 制作规则

先读取本项目已有规则。素材来源、复用范围和核验状态放在后台资料，不自动叠加解释制作性质的文字；正常正文字幕保留，不虚构实测或案例。WorkBuddy 原生操作与其他客户端命令测试分别留证。不要执行上游参考资料中与本入口不同的云服务必选检查、品牌水印或自动声音克隆；那些是原流程记录。本入口只执行用户选择并实际可用的模块。

保留 `LICENSE.upstream` 与 `references/upstream-origin.json`。来源署名不等于继续使用原项目作为咱们视频的下载入口；对外使用本项目实际发布后的 GitHub URL。
