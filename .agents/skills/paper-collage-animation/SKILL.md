---
name: paper-collage-animation
description: Create or revise a short, story-led paper-collage animation in the Paper Collage repository, keeping the editable project and rendered video together.
---

# Paper Collage Animation

Use this skill when the user wants a short paper-collage animation, a new story turned into a video, or a focused revision to an existing scene.

## Start in the repository

Work from the cloned `paper-collage-workbuddy` repository. Confirm that `scripts/workflow.py` and `references/project-schema.en.md` exist before relying on this workflow. If this is an installed skill without the project files, ask the user to open the repository in Codex or provide the project path; do not claim the renderer ran.

For a new story, read `references/story-visual-guide.en.md`, `references/project-schema.en.md`, and `references/workbuddy-workflow.en.md`. For setup and render commands, read `references/quickstart.en.md`. Use the Chinese counterparts when they will help the user.

## Build the story and project

1. Preserve approved copy and narration. Identify the audience, recognizable moment, and intended change in the story. Make the number of shots fit the actual narration instead of forcing every story into the three-shot sample.
2. Create a new project folder. Write its `beats.json` with narration, title, shot duration, framing, camera movement, and distinct actions for each object. Keep changeable text separate from generated artwork.
3. Run `python scripts/workflow.py check PROJECT/beats.json`, then `python scripts/workflow.py plan PROJECT/beats.json OUTPUT_DIR`. The plan command validates inputs and writes a storyboard, asset prompts, motion plan, and report; it does not generate images or video.
4. Prepare separate visual pieces with an image tool available in the current Codex session or with user-supplied assets. Save assets into the project. If image generation is unavailable, provide the prompts and identify the missing assets instead of claiming they exist.
5. Build or revise the editable HyperFrames HTML for the actual story. Animate characters and props as separate elements; each motion should express a story action and settle into a readable end state. Use the repository's example as a reference for technique, not as a substitute for new scenes.
6. Preserve approved narration. When requested by the project, use the local music workflow for instrumental audio. Extend the scene timing when needed; do not truncate speech or silently change the approved voice, words, or pace.
7. Render with `python scripts/workflow.py render ...` using the installed Node, HyperFrames, GSAP, FFmpeg, and FFprobe paths described in `references/quickstart.en.md`. Keep the source beats, editable HTML, assets, audio, final MP4, and run report together.

## Review and deliver

Check the rendered file for complete narration, readable text, visible object movement, transitions, and audio. Report automated checks separately from playback review. If a stage failed, fix that stage and render a new version; do not substitute the included sample for the requested story.

Attribute the story and visual methods inherited from Vox Director as described in `references/adaptation.en.md`. Do not describe a plan, prompt, or still image as a rendered video. Deliver the MP4 with the editable project and reproduction notes.
