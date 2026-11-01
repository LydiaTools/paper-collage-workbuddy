# Setup and your first example

Keep `SKILL.md`, `SKILL.zh-CN.md`, `scripts`, `assets`, `examples`, `references`, and both license files together. Run the commands below from the repository root.

## 1. Inspect the storyboard first

With Python available, validate either language variant and write a planning packet to a new directory. [`beats.json`](../examples/work-focus-layered/beats.json) has Chinese captions; [`beats.en.json`](../examples/work-focus-layered/beats.en.json) has English captions.

```bash
python scripts/workflow.py check examples/work-focus-layered/beats.en.json
python scripts/workflow.py plan examples/work-focus-layered/beats.en.json output/first-plan
```

On systems where Python is named `python3`, use that name instead. Use an empty output directory. The packet contains `storyboard.md`, `asset-prompts.json`, `motion-plan.json`, and `plan-report.json`. This step makes no model calls and does not generate images or video.

Each included plan has three shots totaling 12 seconds at 1280 × 720. Use `title_en` for English and `title_cn` for Chinese. Existing projects with only `title_cn` remain supported.

## 2. Prepare local rendering dependencies

Install Python, Node, FFmpeg, and FFprobe from their official distribution channels if needed. FFmpeg and FFprobe must be in the same directory. The Chinese example needs a CJK font such as Microsoft YaHei or Noto Sans CJK SC; the English example uses a common Latin system font.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm install --prefix .runtime hyperframes@0.8.183 gsap@3.15.0
```

macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npm install --prefix .runtime hyperframes@0.8.183 gsap@3.15.0
```

HyperFrames may download browser dependencies on its first run. Follow its actual setup output.

## 3. Render the supplied project

Replace the FFmpeg path with the actual path on your machine. Use a new output filename for each run.

Windows PowerShell:

```powershell
$nodePath = (Get-Command node).Source
.\.venv\Scripts\python.exe scripts/workflow.py render examples/work-focus-layered/beats.en.json output/first-video-en.mp4 --node "$nodePath" --hyperframes .runtime/node_modules/hyperframes/bin/hyperframes.mjs --gsap .runtime/node_modules/gsap/dist/gsap.min.js --ffmpeg "C:\path\to\ffmpeg.exe"
```

macOS/Linux:

```bash
.venv/bin/python scripts/workflow.py render examples/work-focus-layered/beats.en.json output/first-video-en.mp4 --node "$(command -v node)" --hyperframes .runtime/node_modules/hyperframes/bin/hyperframes.mjs --gsap .runtime/node_modules/gsap/dist/gsap.min.js --ffmpeg "/path/to/ffmpeg"
```

This reproduces the English-captioned three-shot sample with instrumental music. To render the Chinese version, use `beats.json` and a CJK font. Creating a different story requires WorkBuddy to prepare the corresponding assets and editable HTML; changing the titles alone does not create new scenes.

## 4. Open the delivery

Open `output/first-video.mp4` and the adjacent `first-video-assets` directory. The workflow retains the editable project, configuration, music, and run reports.

Watch the complete clip and listen to the sound. Check captions, finished movements, and any narration. The silent `picture.mp4` is an intermediate file; the named final MP4 is the delivery.

For a new topic, start with the English [SKILL.md](../SKILL.md) and [complete workflow](workbuddy-workflow.en.md). Field details are in [project-schema.en.md](project-schema.en.md); audio and sample-renderer settings are in [layered-lifestyle.en.md](layered-lifestyle.en.md). The Chinese versions remain available as `SKILL.zh-CN.md` and the unsuffixed Chinese reference files.
