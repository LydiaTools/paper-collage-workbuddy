---
name: paper-collage-workbuddy
description: Turn an everyday story into an editable paper-collage animation with WorkBuddy, local rendering, and a final MP4.
---

# Paper-Collage Animation with WorkBuddy

This skill adapts the story, beat/shot, and visual-planning ideas in Vox Director into a WorkBuddy workflow with local HyperFrames, GSAP, and FFmpeg rendering. The original Chinese skill is available in [SKILL.zh-CN.md](SKILL.zh-CN.md); the upstream source files and attribution are documented in [the adaptation record](references/adaptation.en.md).

## Choose a starting point

- **A new topic or script:** Follow the [complete workflow](references/workbuddy-workflow.en.md). Plan the story, shots, and object movements, then prepare the assets and editable HTML before rendering with `scripts/workflow.py`.
- **Re-render the included orange-and-teal sample:** Use `examples/work-focus-layered/beats.json` with `renderer: focus-layered`. This route reproduces the supplied three-scene sample; changing its titles does not create a new story.
- **Revise a shot:** Keep approved copy and audio intact. Change only the requested art, movement, composition, or timing, and render a new version.

## Production workflow

1. Define the audience, the moment they recognize, and the result the story should leave them with. Keep an approved script or topic intact; list missing inputs while preparing what can already be done.
2. Use the currently available WorkBuddy model to write `beats.json`: narration, title, scene, duration, shot size, camera movement, and the separate actions of each object. Use the [story and visual guide](references/story-visual-guide.en.md) to choose a structure. Do not pretend a local script called a model.
3. Set a consistent palette, paper texture, and character treatment. The included sample uses orange, deep teal, and cream; use it only when it suits the user's chosen direction. Keep titles on separate text layers so the words can be changed without regenerating the artwork. `workflow.py plan` reuses the included style composer and exports a storyboard, asset prompts, and motion plan; see the [project schema](references/project-schema.en.md).
4. Prepare separate visual pieces with an image tool actually available in WorkBuddy, user-supplied material, or material you may use. If image generation is unavailable, list the missing pieces and prompts; do not say they were generated. Check transparent edges and composition before animation.
5. Create or update editable HyperFrames HTML for the actual shots. Give each character and prop its own movement, triggered by the story and ending in a stable pose. Keep the background and titles steady; do not present a moving full-frame still as independent object animation.
6. By default, generate a complete instrumental track locally. Preserve an approved narration track. If the project specifies Jianying/CapCut narration, use that native workflow; do not silently change the voice, pitch, speed, or approved script. Use `none` only when silence is requested. See [audio and sample settings](references/layered-lifestyle.en.md).
7. Run `workflow.py render` to render the actual animation, mix narration/music, and save the MP4, editable project, storyboard, assets, music, and run report. If the narration is longer than the video, extend the shots first; the renderer must not truncate approved speech silently.
8. Review the final MP4 for readable text, completed movements, transitions, audio, and complete narration. Record technical checks, continuous viewing/listening, and user approval as separate outcomes. Fix a failed stage instead of reusing an older render or delivering the silent intermediate `picture.mp4`.

## Commands and dependencies

```bash
python scripts/workflow.py check examples/work-focus-layered/beats.json
python scripts/workflow.py plan examples/work-focus-layered/beats.json output/first-plan
```

`plan` validates the storyboard inputs and creates `storyboard.md`, `asset-prompts.json`, `motion-plan.json`, and `plan-report.json`. It does not call an image model or create a video.

Render a new editable project with the real dependency paths on your machine:

```bash
python scripts/workflow.py render PROJECT/beats.json output/new-version.mp4 \
  --node PATH_TO_NODE \
  --hyperframes PATH_TO_HYPERFRAMES_MJS \
  --gsap PATH_TO_GSAP_MIN_JS \
  --ffmpeg PATH_TO_FFMPEG
```

The workflow uses Python/Pillow/NumPy, Node, HyperFrames, GSAP, FFmpeg, and FFprobe. Keep FFmpeg and FFprobe together and install a Chinese font when rendering the included Chinese-caption sample. Setup steps are in [Setup and your first example](references/quickstart.en.md). This workflow does not require Atlas Cloud, MiniMax, Veo, or another paid API.

## Useful references

- [Complete production workflow](references/workbuddy-workflow.en.md)
- [Setup and your first example](references/quickstart.en.md)
- [Project fields and commands](references/project-schema.en.md)
- [Layered sample, audio, and motion settings](references/layered-lifestyle.en.md)
- [What was adapted from Vox Director](references/adaptation.en.md)
