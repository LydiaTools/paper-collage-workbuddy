# Story and Visual Guide

This short guide summarizes the parts of the retained Vox Director story and visual notes that apply to this WorkBuddy workflow. The original Chinese research files remain in [`upstream/`](upstream/); see the [adaptation record](adaptation.en.md) for provenance.

## Choose a story shape

Pick a structure that suits the subject instead of forcing each story into the same arc:

| Structure | Useful for | Shape |
| --- | --- | --- |
| `hook_payoff` | One clear idea | Hook → context → build → payoff |
| `pas` | A problem that needs a practical response | Problem → why it matters → solution → evidence → next step |
| `bab` | A visible change | Before → after → bridge → next step |
| `aida` | Introducing something to a new audience | Attention → interest → desire → action |
| `storybrand` | A service or brand story | A person wants something → meets a problem → gets guidance and a plan |
| `how_it_works` | A process or product explanation | Hook → what it is → shown steps → benefit |
| `timeline` | History or a sequence of change | Starting point → events → turning point → present |
| `three_act` | A complete short narrative | Setup → confrontation → resolution |
| `story_circle` | A character's change | Need → search → discovery → return changed |

Let the first scene make the central tension or promise clear. Every beat should add information or change the scene; end when the story has delivered its point. Match shot count and length to the approved script and audio rather than applying a fixed duration formula.

## Plan the picture

- Keep a consistent visual direction across shots: medium, palette, texture, character, and composition.
- Describe objects as distinct paper pieces with clear edges and shadows, so the animator can treat them separately.
- Keep titles and subtitles on their own text layers. The current workflow adds editable text after asset preparation; it does not require image generators to render exact words.
- Choose shot size for the information in that beat: wide to orient, medium to show the main action, close or detail to emphasize one thing.
- Treat camera movement and object movement as separate decisions. `push_in`, `pull_out`, `pan`, `tilt`, `parallax`, and `element` are available sample vocabulary. The actual renderer and HTML determine what runs.
- Give each moving object a clear trigger and a finite action, then let it settle. Keep paper flat and text stable unless the user asks for a different effect.
- When a single shot would need several changes, split it into shots instead of making the animation ambiguous.

The included sample's orange, deep teal, and cream palette is an example, not a required brand direction. Use the user's chosen or approved palette.

## Separate research ideas from product capability

The upstream files preserve research notes and provider-specific prompt examples. They are background material, not evidence that a provider is available here. The local sample renderer creates the supplied layered animation; new image assets and a new editable HTML timeline still need to be prepared for a new story. Follow the current [production workflow](workbuddy-workflow.en.md).
