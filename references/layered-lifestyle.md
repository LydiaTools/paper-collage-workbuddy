# 分层配置与动作

现有版式固定1280×720、60fps，恰好三段，每段至少4秒。入口拒绝不匹配配置；其他画幅、故事关系或短动作需要先修改模板。

## story.json

`character_sheet` 为相对 JSON 的人物图。`palette` 支持 orange、teal、cream、gold，颜色用 CSS 色值。`scenes` 每段包含 seconds、title、subtitle。较长文字先检查是否溢出，不用任意缩小文字掩盖版式问题。

人物素材是2×2透明部件表：左上头部、右上躯干、左下抬手、右下持笔手。比例、方向、姿势及透明边缘需匹配随包图片。新人物先检查静帧和动作短样。

`assets/layered-focus.html` 控制动作：时钟走动、任务堆叠、通知入场、人物响应、进度中断、清除干扰、落笔完成。同一人物和桌面跨段保留，纸张扫过衔接。短震动只用于手机消息，不使用持续随机画面抖动；标题与纸纹稳定。

## 配乐与口播

默认 `audio: {"mode":"generated","mood":"warm-focus","seed":29,"lufs":-20}`。mood 支持 warm-focus、calm、uplifting、reflective；bpm可设60–130。这是参数化器乐合成，不调用云端音乐模型。seed 可复现打击音参数。

使用自己有权使用的音乐：`{"mode":"track","path":"audio/music.wav"}`。短曲会循环并淡入淡出，实际听审循环衔接。只有明确需要静音时使用 `{"mode":"none"}`。

在 audio 中加入 `"narration":"audio/approved-voice.wav"` 可保留口播并压低背景音乐。路径相对 JSON。画面时长应先容纳完整口播：当前混音按画面结束截断，不能把它当作自动改稿功能。

最终 MP4 含 H.264 与 AAC 48kHz立体声。配乐 WAV、HTML 和报告位于成片旁的 assets 目录。报告记录实际运行摘要；完整实际听审和连续观看应另外完成。
