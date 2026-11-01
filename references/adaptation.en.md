# Adaptation from Vox Director

Baseline: Alisa Qian's [Vox Director](https://github.com/Alisa0808/vox-director), commit `6a85a7c341610442a6a5b1885e6e0217ab82a11f`.

| Area | Retained | Added or changed here |
| --- | --- | --- |
| Story and shots | Narrative arcs; beat/shot structure; separate shot size, camera movement, and object movement | Everyday-life and work situations; shot count follows the story and actual audio |
| Visual planning | Original prompt guide, beat-layer notes, and style-composition code | WorkBuddy prepares the plan; user-selected palette; titles remain separate from image assets |
| Execution | A staged path from planning to delivery | WorkBuddy's available model plus local rendering; no required Atlas Cloud API |
| Animation | Layered paper pieces and separate camera/object movement | HyperFrames and GSAP; stable texture and titles; actions settle at their end; new stories get their own HTML project |
| Audio | Separate narration and music | Local instrumental synthesis; preserves an approved narration track; no silent truncation of long speech |
| Delivery | Staged composition of picture, sound, and captions | MP4, storyboard, prompts, movement plan, HTML, assets, music, and run report are kept together |

## Retained upstream files

- `scripts/upstream_styles.py` is based on the upstream `scripts/styles.py`; the workflow calls its `compose_collage_prompt` and `resolve_theme` functions.
- `references/upstream/beat-layer.md` and `references/upstream/prompt-guide.md` are retained in Chinese as source material. English readers can use the concise [story and visual guide](story-visual-guide.en.md).
- `LICENSE.upstream` retains the upstream MIT license.

File-level summaries and hashes are listed in [upstream-origin.json](upstream-origin.json). Older model lists, external links, and research claims in the preserved source notes are not claims about services tested or integrated in this project. The current instructions are in [SKILL.md](../SKILL.md).

## What this project does

This is a workflow skill for an assistant, not a renderer that can invent every asset by itself. The bundled three-scene character sample is wired to the included renderer. A new topic needs WorkBuddy to prepare new shots, assets, and corresponding HTML actions. This version does not integrate MiniMax-H3, Veo, or Atlas Cloud.
