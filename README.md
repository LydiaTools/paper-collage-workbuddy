# 生活职场纸片动画 · Paper Collage for WorkBuddy

**把那些说不清的疲惫，做成看得见的小故事。**

忙了一整天，回头看，最重要的事还停在原地。

刚接上思路，一条消息又把人拉走。下班了，脑子里的待办却还没有关机。

这些感受，写成一句话很容易。想让别人看见那个瞬间，就要再往前走一步：让消息一条条挤进画面，让做到一半的进度退回去，再让人物安静下来，完成眼前的那件事。

这个 Skill 把这段制作流程整理给 WorkBuddy：从选题和文案出发，安排分镜、准备素材、设计动作，再把画面和声音合成一段动画。你可以打开工程，继续改到它更像你想表达的样子。

![随包样片预览：橙、深青绿与奶油白的生活职场纸片动画](media/preview.jpg)

**[先看 12 秒带配乐样片](media/work-focus-12s.mp4)** · [下载整个 Skill](https://github.com/LydiaTools/paper-collage-workbuddy/archive/refs/heads/main.zip) · [阅读 SKILL.md](SKILL.md)

本项目基于 [Vox Director](https://github.com/Alisa0808/vox-director) 改造，保留其故事、分镜与视觉方法，补上 WorkBuddy 执行流程、本地分层动画和配乐交付。[具体继承与改动](references/adaptation.md)均保留记录。

## 先从一个熟悉的故事开始

随包的样片讲的是：**为什么忙了一天，正事却没做完。**

| 你想说的话 | 画面怎样接住它 |
| --- | --- |
| 忙了一整天，正事没动 | 任务纸张、消息卡和时钟轮流出现，把人物围在中间 |
| 一被打断，就要重来 | 手机通知打断动作，进度退回，人物停下来 |
| 先完成最重要的那件 | 杂事退出画面，落笔、完成，最后出现一个对勾 |

三段，每段 4 秒。橙、深青绿、奶油白，配上本地生成的器乐。

你可以先复跑这个例子，看看一份文案怎样变成分镜，分镜又怎样落到人物和道具的动作上。做新选题时，再为那个故事准备它自己的场景和动作。

## 把力气留给想表达的那句话

做这类短片，费劲的地方常常藏在细节里：标题跟着图片跑，人物一直晃，改完画面又要重配音乐，下一次想继续做，却找不到能接着改的工程。

这份 Skill 围绕这些环节整理了制作方式：

- **文字能单独改。** 标题独立成层，图片素材不烧录标题，改一句话时可以保留画面。
- **动作有开始，也有结束。** 人物、纸张、通知和道具分层安排，按故事先后行动，完成后停稳。
- **声音跟着表达走。** 可生成器乐配乐；已有认可的口播就沿用，混音时让音乐在人声下面。
- **成片之后，还能接着做。** 交付带音轨的 MP4，也保留可编辑 HTML、分镜、素材、独立配乐和运行报告。

适合拿来做生活观察、职场感受，以及一个小方法的解释短片。你带来想说的事，WorkBuddy 按流程组织制作；新素材和新动作仍需要由它实际调用可用工具来完成。

## 让 WorkBuddy 开始第一段

1. [下载仓库 ZIP](https://github.com/LydiaTools/paper-collage-workbuddy/archive/refs/heads/main.zip)，解压后把文件夹命名为 `paper-collage-workbuddy`。
2. 将整个文件夹放入 WorkBuddy 当前配置的技能目录。Windows 常见位置是 `%USERPROFILE%\.workbuddy\skills`，以应用设置为准；打开文件夹就应能看到 `SKILL.md`。
3. 按[上手流程](references/quickstart-layered.md)准备依赖，先复跑随包样片，再换成自己的选题。

想做新故事时，可以直接把这段话交给 WorkBuddy：

> 使用 paper-collage-workbuddy，做一段生活职场纸片动画。选题是“下班后，消息还在追着你跑”。先围绕这个具体烦恼写文案，列出分镜和每个物件的动作，沿用橙、深青绿、奶油白。等我确认文案后，再准备素材和可编辑工程，实际渲染带配乐的 MP4。每个场景按这个故事重新设计，保留我已有的口播，并把分镜、素材、独立配乐和工程一起交给我。

想先看看制作过程，也可以只说：

> 用随包样片给我讲清楚：这三句话为什么这样拆镜头，每个动作分别在表达什么。先出分镜表。

## 想继续改，可以从这里找

| 你接下来要做的事 | 入口 |
| --- | --- |
| 安装依赖、复跑第一段样片 | [上手流程](references/quickstart-layered.md) |
| 从新选题走到最终成片 | [完整制作流程](references/workbuddy-workflow.md) |
| 修改分镜、时长、声音和渲染配置 | [项目参数](references/project-schema.md) |
| 看看相对原项目改了什么 | [二次开发记录](references/adaptation.md) |

本地制作使用 Python、Node、HyperFrames、GSAP 和 FFmpeg，首次运行需准备相应依赖与中文字体。故事和素材由 WorkBuddy 的实际模型及可用工具组织，脚本负责校验、提示词组合、渲染与合成。默认流程不要求 Atlas Cloud API，当前没有接入 MiniMax、Veo 等视频生成服务。

随包提供的是一段 12 秒、三镜头的具体例子。新故事的镜头数量、画幅、素材和编舞按内容重新安排；安装与复跑步骤见上面的指南。

## 感谢与来源

感谢 **Alisa Qian** 的 [Vox Director](https://github.com/Alisa0808/vox-director)。本项目继承了它的叙事弧、beats/shots 分镜体系、视觉提示词资料与风格组合代码，并在此基础上整理 WorkBuddy 版本。

上游基线：`6a85a7c341610442a6a5b1885e6e0217ab82a11f`。继承文件与摘要见[来源记录](references/upstream-origin.json)，原 MIT 许可保留于 [LICENSE.upstream](LICENSE.upstream)，新增代码按 [LICENSE](LICENSE) 发布。

示例人物由图像工具生成并整理成部件，配乐由本地器乐合成生成；包内不包含参考视频的画面或声音。

如果你用它讲出了一个自己的故事，欢迎在 [Issues](https://github.com/LydiaTools/paper-collage-workbuddy/issues) 分享做法、遇到的问题，或你希望继续改进的地方。
