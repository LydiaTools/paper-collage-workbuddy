# Paper Collage for WorkBuddy

[简体中文](README.zh-CN.md) · **English**

**Give a familiar feeling a scene of its own.**

Turn a story into a paper collage video with WorkBuddy, and keep the editable project alongside the MP4.

You've been busy all day. The one task that mattered is still sitting there.

You finally find your train of thought. A notification arrives. Now you have to find it again.

A short animation can make that moment visible: messages crowd the desk, progress slips back, and eventually the distractions leave enough room to finish one thing.

This WorkBuddy skill organizes the steps from an idea to a paper collage animation: story, shots, separate visual pieces, movement, music, and a rendered video. It keeps the editable project alongside the MP4, so the next change can start where you left off.

![A silent excerpt of the included orange, teal, and cream animation, with Chinese captions](media/preview-motion.gif)

*Six-second silent preview from the included sample. The full 12-second video has music and Chinese captions.*

**[Download the full example with music](https://raw.githubusercontent.com/LydiaTools/paper-collage-workbuddy/main/media/work-focus-12s.mp4)** · [Download the skill](https://github.com/LydiaTools/paper-collage-workbuddy/archive/refs/heads/main.zip) · [Setup and first run](references/quickstart.en.md)

Adapted from **Alisa Qian's [Vox Director](https://github.com/Alisa0808/vox-director)**, with its story and visual methods retained and a WorkBuddy workflow, local layered animation, and music delivery added. [See the adaptation record](references/adaptation.md).

## Start with a story you recognize

The included example asks: **Why did a whole busy day leave the important work unfinished?**

| Story beat | What happens on screen |
| --- | --- |
| Busy all day, important work untouched | Task sheets, messages, and a clock surround the character. |
| An interruption means starting again | A phone notification interrupts the action; progress resets. |
| Finish the one thing that matters | Distractions leave, the character writes, and a check mark appears. |

Three shots, four seconds each. Orange, deep teal, cream, and locally synthesized instrumental music. The supplied video and project captions are in Chinese; the table above translates their meaning.

Run that example first, then use its structure to understand how a sentence becomes a shot and a shot becomes movement. A new story needs its own assets and choreography.

## Keep your attention on what you want to say

- **Edit words separately.** Titles remain text layers, so changing a sentence can leave the illustration intact.
- **Give movement a purpose.** Characters and props move in sequence and settle when their action is done.
- **Keep the voice you chose.** Use an existing narration track and mix generated instrumental music underneath it.
- **Keep the work editable.** Save the MP4, HTML project, storyboard, assets, music, and run report together.

The workflow suits small stories about everyday life, work, and practical habits. WorkBuddy's available model and tools prepare the story, imagery, and motion project; the Python scripts validate plans, assemble prompts, render, and mix audio.

## Try it with WorkBuddy

1. Download the ZIP and rename the extracted folder to `paper-collage-workbuddy`.
2. Place the whole folder in WorkBuddy's configured skills directory. `SKILL.md` should sit directly inside it. A common Windows location is `%USERPROFILE%\.workbuddy\skills`; check your application settings.
3. Follow the [English setup guide](references/quickstart.en.md) to inspect the plan and reproduce the included example.

For a new topic, try this prompt:

> Use paper-collage-workbuddy to make a short paper collage animation about "The workday ends, but the notifications don't." First write the story, shot list, and individual object movements in English. Use orange, deep teal, and cream. Let me review the script before preparing assets and the editable animation project. Then render an MP4 with instrumental music. Preserve any narration I supply, and include the storyboard, assets, music, and editable project in the delivery.

If you want to explore before rendering:

> Read the included example and explain how its three story beats become shots. Give me a storyboard table first.

The skill and detailed production references are currently written in Chinese. You can ask WorkBuddy to explain them in English. Native English-language execution in WorkBuddy has not been separately verified.

## What you need

Local rendering uses Python, Node, HyperFrames, GSAP, and FFmpeg. The supplied example also needs a Chinese font. The [setup guide](references/quickstart.en.md) includes dependency versions and commands. This version does not require an Atlas Cloud API account and has no MiniMax or Veo integration.

The repository includes one concrete 12-second project. For a new topic or aspect ratio, prepare the scenes and motion for that content before rendering.

## Credits

Thank you to **Alisa Qian** for Vox Director's narrative arcs, beats/shots structure, visual prompt references, and style-composition code.

Upstream baseline: `6a85a7c341610442a6a5b1885e6e0217ab82a11f`. Inherited files and hashes are recorded in [upstream-origin.json](references/upstream-origin.json). The original MIT notice is retained in [LICENSE.upstream](LICENSE.upstream); added code is covered by [LICENSE](LICENSE).

The example character was generated with an image tool and arranged into separate parts. Its instrumental music was synthesized locally. Reference-video footage and audio are not included.

If you try the workflow, [share the story you made or the step that got in your way](https://github.com/LydiaTools/paper-collage-workbuddy/issues).
