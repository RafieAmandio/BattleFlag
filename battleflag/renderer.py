"""Video renderer using Pillow and MoviePy."""

import os

from PIL import Image, ImageDraw, ImageFont
import numpy as np

from config import (
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
    FPS,
    BACKGROUND_COLOR,
    FONT_SIZE_TITLE,
    FONT_SIZE_SCORE,
    FONT_COLOR,
    OUTPUT_DIR,
    OUTPUT_FORMAT,
)


def render_frame(frame_data, title="Pertarungan Lingkaran"):
    """Render a single frame as a PIL Image."""
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Title text
    try:
        font_title = ImageFont.truetype("assets/fonts/bold.ttf", FONT_SIZE_TITLE)
        font_score = ImageFont.truetype("assets/fonts/bold.ttf", FONT_SIZE_SCORE)
    except (OSError, IOError):
        font_title = ImageFont.load_default()
        font_score = ImageFont.load_default()

    # Draw title
    bbox = draw.textbbox((0, 0), title, font=font_title)
    text_width = bbox[2] - bbox[0]
    draw.text(
        ((VIDEO_WIDTH - text_width) // 2, 80),
        title,
        fill=FONT_COLOR,
        font=font_title,
    )

    # Draw circles
    for circle in frame_data:
        x, y, r = int(circle["x"]), int(circle["y"]), int(circle["radius"])
        color = circle["color"]
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color, outline=(255, 255, 255), width=2)

        # Draw name inside circle
        name = circle["name"]
        name_bbox = draw.textbbox((0, 0), name, font=font_score)
        name_w = name_bbox[2] - name_bbox[0]
        name_h = name_bbox[3] - name_bbox[1]
        if name_w < r * 2:
            draw.text(
                (x - name_w // 2, y - name_h // 2),
                name,
                fill=(255, 255, 255),
                font=font_score,
            )

    # Draw scoreboard
    sorted_circles = sorted(frame_data, key=lambda c: c["score"], reverse=True)
    y_offset = VIDEO_HEIGHT - 300
    draw.text((40, y_offset - 40), "Skor:", fill=FONT_COLOR, font=font_score)
    for i, c in enumerate(sorted_circles[:5]):
        score_text = f"{c['name']}: {c['score']}"
        draw.text((40, y_offset + i * 45), score_text, fill=c["color"], font=font_score)

    return img


def render_video(frames, output_name="battle", title="Pertarungan Lingkaran"):
    """Render all frames into an MP4 video."""
    from moviepy.editor import ImageSequenceClip

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    rendered_frames = []
    for frame_data in frames:
        img = render_frame(frame_data, title=title)
        rendered_frames.append(np.array(img))

    clip = ImageSequenceClip(rendered_frames, fps=FPS)
    output_path = os.path.join(OUTPUT_DIR, f"{output_name}.{OUTPUT_FORMAT}")
    clip.write_videofile(output_path, codec="libx264", audio=False)
    return output_path
