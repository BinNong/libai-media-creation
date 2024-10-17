import asyncio

import edge_tts
import moviepy.editor as mp
import os
from moviepy.editor import TextClip, VideoFileClip

def create_video(video_path, audio_script_path, bg_music_path, subtitles_path, output_path):
    print("Loading video...")
    video = mp.VideoFileClip(video_path)
    
    print("Generating speech from script...")
    with open(audio_script_path, 'r', encoding='utf-8') as audio_script_file:
        audio_script = audio_script_file.read()
    generate_audio(audio_script)  # Change to .wav
    
    # Update debug logging
    import os
    if os.path.exists("temp_speech.wav"):
        print(f"temp_speech.wav exists. File size: {os.path.getsize('temp_speech.wav')} bytes")
    else:
        print("temp_speech.wav does not exist!")

    speech = mp.AudioFileClip("temp_speech.wav")  # Change to .wav
    
    # Load background music
    print("Loading background music...")
    bg_music = mp.AudioFileClip(bg_music_path)
    
    # Adjust background music length to match video length
    if bg_music.duration > video.duration:
        bg_music = bg_music.subclip(0, video.duration)
    else:
        bg_music = bg_music.audio_loop(duration=video.duration)
    
    # Mix speech and background music
    print("Mixing audio...")
    bg_music = bg_music.volumex(0.1)  # Lower the volume of background music
    final_audio = mp.CompositeAudioClip([speech, bg_music])
    
    # If the raw video is too short, repeat it to match the duration of audio
    if video.duration < final_audio.duration:
        video = video.loop(duration=final_audio.duration)
    
    # Add audio to video
    print("Adding audio to video...")
    final_video = video.set_audio(final_audio)
    
    # Add subtitles
    print("Adding subtitles...")
    with open(subtitles_path, 'r', encoding='utf-8') as subtitles_file:
        subtitles = subtitles_file.read()
    
    def add_subtitles(gf, txt):
        print(TextClip.list('font'))
        # Create a TextClip for each line of subtitles
        txt_clips = [TextClip(line, fontsize=24, color='red', font='PingFang-SC-Semibold', method='label', size=video.size)
                     .set_position(('center', 'bottom')).set_start(i*2).set_duration(2)
                     for i, line in enumerate(txt.splitlines()) if line.strip() != '']
        # Overlay text clips on the video
        return mp.CompositeVideoClip([gf] + txt_clips)

    final_video = add_subtitles(final_video, subtitles)
    
    # Before writing the final video, ensure the duration is set
    if final_video.duration is None:
        final_video.duration = final_video.audio.duration

    # Write the result to a file
    print(f"Writing final video to {output_path}...")
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    # Clean up temporary files
    os.remove("temp_speech.wav")
    print("Video creation completed!")


def generate_audio(text: str, model_name: str="zh-CN-YunxiNeural") -> None:
    async def _generating() -> None:
        communicate = edge_tts.Communicate(text, model_name)
        await communicate.save("temp_speech.wav")

    asyncio.run(_generating())
