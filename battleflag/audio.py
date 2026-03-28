"""Audio integration for battle videos."""

import os

from pydub import AudioSegment


def add_audio_to_video(video_path, audio_path, output_path=None):
    """Combine a video file with a background audio track."""
    from moviepy.editor import VideoFileClip, AudioFileClip

    if output_path is None:
        base, ext = os.path.splitext(video_path)
        output_path = f"{base}_with_audio{ext}"

    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Loop or trim audio to match video duration
    if audio.duration < video.duration:
        loops_needed = int(video.duration / audio.duration) + 1
        audio_segment = AudioSegment.from_file(audio_path)
        looped = audio_segment * loops_needed
        temp_audio = "temp/looped_audio.mp3"
        os.makedirs("temp", exist_ok=True)
        looped.export(temp_audio, format="mp3")
        audio = AudioFileClip(temp_audio)

    audio = audio.subclip(0, video.duration)
    final = video.set_audio(audio)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

    video.close()
    audio.close()
    return output_path
