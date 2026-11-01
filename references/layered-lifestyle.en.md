# Layered Sample, Audio, and Motion Settings

## The included `story.json` sample

The bundled sample uses 1280×720 at 60 fps and exactly three scenes of at least four seconds each. The sample renderer rejects configurations outside those limits. For another story, duration, or aspect ratio, adapt the template and choreography instead of cropping or stretching the existing sample.

`character_sheet` points to a character sprite sheet relative to the JSON file. `palette` accepts `orange`, `teal`, `cream`, and `gold`, or CSS color values. Each scene has `seconds`, `title`, and `subtitle`. Check that longer copy fits; do not hide layout problems by shrinking type without review.

The character sheet is a 2×2 transparent sprite sheet: head upper left, torso upper right, raised hand lower left, writing hand lower right. New character art should match the proportions, direction, pose, and transparent edges expected by the sample. Check a still and a short motion sample first.

`assets/layered-focus.html` animates the sample: clock movement, task sheets piling up, a notification arriving, the character reacting, progress being interrupted, distractions leaving, and the final writing action. The same character and desk continue across scenes, with a paper wipe between them. Use a short shake for the phone notification only; keep the title and paper texture steady.

## Music and narration

Default sample settings:

```json
{"mode":"generated","mood":"warm-focus","seed":29,"lufs":-20}
```

Supported moods are `warm-focus`, `calm`, `uplifting`, and `reflective`; `bpm` may be set from 60 to 130. This is parameterized local instrumental synthesis, not a cloud music model. The seed makes percussion parameters reproducible.

Use music you may use with `{"mode":"track","path":"audio/music.wav"}`. Short tracks loop with fades; listen to the join. Use `{"mode":"none"}` only when silence is requested.

Add approved speech with `"narration":"audio/approved-voice.wav"` in `audio`. The path is relative to the JSON file, and the mix lowers background music under narration. Extend the video to fit the full narration: the current mixer trims to the video end and does not rewrite the script for you.

The final MP4 contains H.264 video and 48 kHz stereo AAC audio. The music WAV, editable HTML, and run report are saved in the MP4's neighboring assets folder. A report is not a substitute for listening to the complete result or watching it through.
