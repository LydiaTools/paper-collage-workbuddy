# Complete WorkBuddy Production Workflow

## Inputs and project folder

Start from a topic, an approved script, or an approved audio track. Check what already exists and do not rewrite approved material. Create a new project folder, keep paths relative to `beats.json`, and never overwrite an earlier version.

1. **Story:** Read the [story and visual guide](story-visual-guide.en.md). Build a clear situation, development, turning point, and outcome around the topic. Choose an arc that fits; do not force every topic into an advertisement. Let the story and supplied audio determine the number of shots.
2. **Shots:** Ask WorkBuddy's currently available model to write `beats.json`. For each shot, specify its scene, framing, duration, camera move, object actions, and the result of those actions. Preserve any approved narration exactly. Fit the visuals to the actual audio timing.
3. **Visual direction:** Use a palette the user has chosen or approved. The supplied sample uses orange, deep teal, and cream. Use distinct props, clear cutout edges, paper texture, and a consistent character. Add titles and captions later as text layers; do not bake changing copy into generated artwork.
4. **Prepare assets:** Run `workflow.py plan` to export a storyboard, asset prompts, and a movement plan. This command does not call an image model. Use an image tool actually available in WorkBuddy, user material, or material you may use to create the individual pieces. Record any missing pieces honestly.
5. **Animate:** Create `editable/index.html` for the new story and implement its actual shots as a HyperFrames timeline. Use relative `assets/gsap.min.js` and project assets. Set the root width, height, frame rate, duration, and `window.__timelines.main`. Animate separate paper pieces instead of repeatedly moving the whole illustration. Give each action a start, a finite easing, and a settled end state.
6. **Music and narration:** By default, create a continuous instrumental track locally. Add approved speech as `audio.narration`; if the project specifies Jianying/CapCut narration, follow that native workflow. Do not substitute a voice, change pitch or speed, or regenerate approved copy. Extend the shots when needed to fit the full narration.
7. **Render:** Run `workflow.py render` to validate the HTML, render at 60 fps, mix the audio, and write the final video. Keep any error and repair the stage that failed. Never substitute an older MP4 or deliver the silent `picture.mp4` intermediate.
8. **Deliver and review:** Deliver the final MP4, editable HTML, `beats.json`, assets, separate music, run report, and steps for reproducing this version. Check text, story events, movement, transitions, and sound. Log automated checks separately from continuous viewing/listening and user acceptance.

## Two rendering routes

`focus-layered` is for the included, verified three-scene “busy → interrupted → focused” sample. `hyperframes` is for a new story with its own shots and editable HTML. If the new story lacks assets or HTML, do not fall back to the sample and change only its headings.

This skill does not automatically start a cloud-generation task. A new paid service or account connection requires the user's choice.
