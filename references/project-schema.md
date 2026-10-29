# 项目字段与命令

保留上游 `project`、`topic`、`language`、`aspect`、`theme`、`arc`、`beats`、`shots` 结构。每段需要唯一 id、title_cn、narration；每镜需要 id、dur、shot_size、camera_move、scene、element_motion。

新增本地字段：width、height、renderer、editable_project、audio。`renderer` 为 `hyperframes` 或随包专用 `focus-layered`。前者需要 WorkBuddy 创建真实的可编辑工程；工程尺寸和总时长必须与分镜一致。后者需要 character_sheet，固定三段、1280×720、各至少4秒。

支持景别 EST_WIDE、WIDE、MEDIUM、CLOSE、DETAIL；平面运镜 static、push_in、pull_out、pan、tilt、parallax、element。物件动作单独写 element_motion，不用换运镜掩盖画面没有独立动作。

```json
{
  "project":"new-story", "topic":"生活职场中的具体烦恼", "language":"zh",
  "aspect":"16:9", "width":1280, "height":720,
  "theme":"atomic-age", "arc":"hook_payoff",
  "renderer":"hyperframes", "editable_project":"editable",
  "audio":{"mode":"generated","mood":"warm-focus","seed":29},
  "beats":[
    {"id":1,"title_cn":"一个具体烦恼","narration":"已确认正文。",
     "shots":[{"id":"a","dur":4,"shot_size":"WIDE","camera_move":"static",
       "scene":"按本期故事准备的人物与道具",
       "element_motion":"分别写出每件物体的动作、触发和结果"}]}
  ]
}
```

上面的 JSON 只说明字段，完整画面需要真实素材和 HTML，不能把字段示意直接当成已完成工程。可运行案例见 examples/work-focus-layered/beats.json。

`python scripts/workflow.py check 项目/beats.json` 校验数据。

`python scripts/workflow.py plan 项目/beats.json 新计划目录` 输出 storyboard.md、asset-prompts.json、motion-plan.json 和 plan-report.json；不生成图片或视频。

`python scripts/workflow.py render 项目/beats.json 新版本.mp4 --node Node路径 --hyperframes hyperframes.mjs路径 --gsap gsap.min.js路径 --ffmpeg FFmpeg路径` 实际渲染并混音。

audio 支持 generated、track、none，情绪与口播参数见 layered-lifestyle.md。既有 narration 长于实际画面时脚本会报错，先调整镜头，不能截掉已批准台词。
