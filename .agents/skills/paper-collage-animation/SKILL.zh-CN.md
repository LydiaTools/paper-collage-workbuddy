# 纸片动画

用户想制作一段有故事的纸片动画、把一个新故事做成视频，或只修改现有场景时使用。

## 先确认项目位置

在完整克隆的 `paper-collage-workbuddy` 仓库中工作。开始前确认 `scripts/workflow.py` 和 `references/project-schema.en.md` 存在。如果当前只安装了 Skill 文件、没有项目文件，请让用户在 Codex 中打开仓库或提供工程路径；不要声称渲染器已经运行。

制作新故事时，阅读 `references/story-visual-guide.md`、`references/project-schema.md` 和 `references/workbuddy-workflow.md`。准备依赖和渲染时，阅读 `references/quickstart-layered.md`。这些制作资料包含部分 WorkBuddy 操作说明；只复用故事与制作流程，不把 WorkBuddy 菜单写成 Codex 操作步骤。

## 制作故事和工程

1. 保留用户已确认的文案和口播。明确目标受众、能让人认出的具体时刻，以及故事希望带来的变化。镜头数按口播时长决定，不把新故事硬塞进三镜头样片。
2. 新建工程目录，编写 `beats.json`，包含口播、标题、镜头时长、景别、镜头运动和每个物件各自的动作。可修改的文字单独保留，不烘焙进插画。
3. 运行 `python scripts/workflow.py check PROJECT/beats.json`，再运行 `python scripts/workflow.py plan PROJECT/beats.json OUTPUT_DIR`。plan 会校验输入并输出分镜表、素材提示词、动作计划和报告；它不会生成图片或视频。
4. 使用当前 Codex 会话实际可用的图像工具，或用户提供的素材，准备独立的画面元素并存进工程。如果没有可用的图像生成工具，就给出提示词并列出缺少的素材，不要声称素材已经生成。
5. 为实际故事创建或修改可编辑的 HyperFrames HTML。人物和道具分开运动；每个动作表达一个故事行为，并停在清楚可读的状态。样片只作制作方法参考，不替代新故事的场景。
6. 保留已确认的口播。项目需要配乐时，按本地音乐流程制作器乐。口播较长就延长镜头；不要截断语音，也不要暗中改动确认过的声音、文字或语速。
7. 按 `references/quickstart-layered.md` 中的说明，使用已安装的 Node、HyperFrames、GSAP、FFmpeg 和 FFprobe 路径运行 `python scripts/workflow.py render ...`。把源分镜、可编辑 HTML、素材、音频、最终 MP4 和运行报告一起保存。

## 检查和交付

检查成片是否包含完整口播、可读文字、清楚的物件动作、转场和声音。自动检查与实际播放/收听结果分开记录。某个环节失败就修复该环节并重新渲染，不要拿随包样片代替用户要求的新故事。

按 `references/adaptation.md` 标注继承自 Vox Director 的故事与视觉方法。不要把计划、提示词或静帧称作已渲染视频。交付 MP4、可编辑工程和复现说明。
