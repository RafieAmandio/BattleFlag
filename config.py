"""Global configuration for the BattleFlag video pipeline."""

# Video dimensions (9:16 vertical for TikTok/Shorts/Reels)
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# Battle settings
CIRCLE_MIN_RADIUS = 40
CIRCLE_MAX_RADIUS = 120
BATTLE_DURATION_SEC = 30
BACKGROUND_COLOR = (15, 15, 25)

# Text overlay (Bahasa Indonesia)
FONT_SIZE_TITLE = 72
FONT_SIZE_SCORE = 48
FONT_COLOR = (255, 255, 255)
TEXT_POSITION_TITLE = ("center", 100)
TEXT_POSITION_SCORE = ("center", 200)

# Output
OUTPUT_DIR = "output"
TEMP_DIR = "temp"
OUTPUT_FORMAT = "mp4"
OUTPUT_CODEC = "libx264"
AUDIO_CODEC = "aac"
