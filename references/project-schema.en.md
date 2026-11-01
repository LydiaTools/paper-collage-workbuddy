# Project Fields and Commands

Keep the upstream `project`, `topic`, `language`, `aspect`, `theme`, `arc`, `beats`, and `shots` structure. Each beat needs a unique `id`, a localized title (`title_en` for English or `title_cn` for Chinese), and `narration`. Existing projects using only `title_cn` remain supported. Optional `subtitle_en` and `subtitle_cn` fields set on-screen captions; if omitted, narration is used. Each shot needs `id`, `dur`, `shot_size`, `camera_move`, `scene`, and `element_motion`.

Additional local fields are `width`, `height`, `renderer`, `editable_project`, and `audio`. `renderer` is `hyperframes` for a new editable project or `focus-layered` for the supplied sample. The HyperFrames route requires a real editable project whose dimensions and duration match the storyboard. The sample renderer requires a `character_sheet`, exactly three scenes, 1280×720, and at least four seconds per scene.

Supported shot sizes: `EST_WIDE`, `WIDE`, `MEDIUM`, `CLOSE`, `DETAIL`. Supported camera moves: `static`, `push_in`, `pull_out`, `pan`, `tilt`, `parallax`, `element`. Specify object movement separately in `element_motion`; do not use a camera move to imply that objects move independently.

```json
{
  "project": "new-story",
  "topic": "a specific everyday work problem",
  "language": "en",
  "aspect": "16:9",
  "width": 1280,
  "height": 720,
  "theme": "atomic-age",
  "arc": "hook_payoff",
  "renderer": "hyperframes",
  "editable_project": "editable",
  "audio": {"mode": "generated", "mood": "warm-focus", "seed": 29},
  "beats": [
    {
      "id": 1,
      "title_en": "one specific problem",
      "narration": "Approved narration goes here.",
      "shots": [
        {
          "id": "a",
          "dur": 4,
          "shot_size": "WIDE",
          "camera_move": "static",
          "scene": "Characters and props prepared for this story",
          "element_motion": "Describe each object's trigger, movement, and settled result."
        }
      ]
    }
  ]
}
```

This example shows the data shape only. A finished scene still needs real assets and editable HTML. See `examples/work-focus-layered/beats.json` for a runnable bundled example.

```bash
python scripts/workflow.py check PROJECT/beats.json
python scripts/workflow.py plan PROJECT/beats.json output/new-plan
python scripts/workflow.py render PROJECT/beats.json output/new-version.mp4 \
  --node PATH_TO_NODE --hyperframes PATH_TO_HYPERFRAMES_MJS \
  --gsap PATH_TO_GSAP_MIN_JS --ffmpeg PATH_TO_FFMPEG
```

`plan` creates `storyboard.md`, `asset-prompts.json`, `motion-plan.json`, and `plan-report.json`; it does not create images or video. Audio modes are `generated`, `track`, and `none`; see [layered sample and audio settings](layered-lifestyle.en.md). If approved narration exceeds the rendered duration, the renderer reports an error. Extend the shots; do not cut off the approved words.
