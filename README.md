# 生活职场动画 Skill · WorkBuddy 完整优化版

这是在 [Vox Director](https://github.com/Alisa0808/vox-director) 基础上改造的 Skill。保留原来的叙事弧、beats/shots分镜体系、视觉提示词方法及风格组合器，改为由 WorkBuddy 自身模型组织项目，使用平稳分层动画、HyperFrames、原创器乐与 FFmpeg 完成制作。

![橙绿生活职场动画](media/preview.jpg)

[Skill 本体](SKILL.md) · [完整制作流程](references/workbuddy-workflow.md) · [二次开发改动表](references/adaptation.md) · [12秒带配乐样片](media/work-focus-12s.mp4)

## 使用方式

下载整个仓库或安装包，将包含 SKILL.md 的文件夹命名为 `paper-collage-workbuddy`，放入 WorkBuddy 当前配置的技能目录。Windows 常见位置为 `%USERPROFILE%\.workbuddy\skills`；以应用当前设置为准，不多套一层目录。

直接告诉 WorkBuddy：

> 使用 paper-collage-workbuddy，按完整制作流程制作一个生活职场话题动画。选题是“下班后，消息还在追着你跑”。先围绕受众的具体烦恼组织文案、分镜与独立动作，沿用橙、深青绿、奶油白。确认文案后准备素材和 HyperFrames 工程，实际渲染带配乐 MP4，并交付可编辑文件和制作流程。不同故事重新设计场景和动作，不只改旧样片标题；已有口播保持不变。

新选题的故事、镜头、素材和编舞由 WorkBuddy 的实际模型与可用工具执行。脚本负责校验、提示词组合、渲染和合成；不把规则脚本称作内置大模型。

## 已接通的优化

- 保留上游主题→分镜→视觉→动画→声音→合成体系，并直接复用上游风格提示词组合代码。
- 增加 WorkBuddy 中文执行入口、可交付分镜表、素材提示词和动作计划。
- 标题与图片分离，固定纹理；物件按事件运动，结束停稳，60fps渲染。
- 生成原创器乐，保留已认可口播并自动压低背景音乐；旁白超出画面时拒绝静默截断。
- 保留可编辑 HTML、beats.json、素材、配乐和实际运行报告，便于继续换选题迭代。

随包12秒样片使用已验证的三段人物编舞，新选题使用 `renderer: hyperframes` 和新工程，不限制为三个镜头。新场景的图片或人物表演仍需要真实素材和具体编舞，不能仅修改标题就保证任意故事自动完成。

依赖准备与复跑命令见 [上手流程](references/quickstart-layered.md)，字段见 [项目参数](references/project-schema.md)。默认流程无需 Atlas Cloud API；本包没有接入 MiniMax、Veo 等服务。

## 来源与许可

上游基线为 Vox Director `6a85a7c341610442a6a5b1885e6e0217ab82a11f`；继承文件的实际摘要见 [来源记录](references/upstream-origin.json)。上游 MIT 许可保留于 [LICENSE.upstream](LICENSE.upstream)，本包新增代码按 [LICENSE](LICENSE) 发布。示例人物由图像工具生成并整理成部件，配乐由本地器乐合成生成；不包含参考视频的画面或声音。
