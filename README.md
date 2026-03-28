# BattleFlag - Battling Circles Video Pipeline

Automated video generation engine for faceless "battling circles" content targeting Indonesian social media (TikTok, YouTube Shorts, Reels).

Circles representing countries/teams battle each other on screen — colliding, absorbing, and competing until one champion remains. All text overlays are in Bahasa Indonesia.

## Prerequisites

- **Python 3.10+**
- **FFmpeg** installed and available in PATH
  - macOS: `brew install ffmpeg`
  - Ubuntu: `sudo apt install ffmpeg`
  - Windows: [Download from ffmpeg.org](https://ffmpeg.org/download.html)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RafieAmandio/BattleFlag.git
cd BattleFlag
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate a battle video

```bash
python main.py
```

This generates a 30-second battle video in `output/battle.mp4`.

### Options

```bash
python main.py --circles 10        # Number of competing circles (default: 8)
python main.py --output my_battle  # Custom output filename
python main.py --title "Perang!"   # Custom title overlay
```

## Project Structure

```
BattleFlag/
├── main.py                  # Entry point
├── config.py                # Global settings (resolution, FPS, colors)
├── requirements.txt         # Python dependencies
├── battleflag/
│   ├── __init__.py
│   ├── circle.py            # Circle entity (movement, collision, absorption)
│   ├── battle.py            # Battle simulation engine
│   ├── renderer.py          # Video frame rendering (Pillow + MoviePy)
│   └── audio.py             # Audio integration (background music)
├── assets/
│   ├── fonts/               # Custom fonts (place .ttf files here)
│   └── audio/               # Background music tracks
├── scripts/                 # Utility/batch scripts
└── output/                  # Generated videos (git-ignored)
```

## Configuration

Edit `config.py` to customize:

| Setting | Default | Description |
|---------|---------|-------------|
| `VIDEO_WIDTH` | 1080 | Video width in pixels |
| `VIDEO_HEIGHT` | 1920 | Video height (9:16 vertical) |
| `FPS` | 30 | Frames per second |
| `BATTLE_DURATION_SEC` | 30 | Battle length in seconds |
| `CIRCLE_MIN_RADIUS` | 40 | Minimum circle size |
| `CIRCLE_MAX_RADIUS` | 120 | Maximum circle size |

## Adding Custom Fonts

Place `.ttf` font files in `assets/fonts/` and rename to `bold.ttf` for the renderer to pick up automatically.

## Adding Background Music

Place audio files in `assets/audio/` and use the audio module:

```python
from battleflag.audio import add_audio_to_video

add_audio_to_video("output/battle.mp4", "assets/audio/track.mp3")
```

## License

MIT
