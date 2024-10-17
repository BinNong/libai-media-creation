import argparse
from video_utils import create_video

def main():
    parser = argparse.ArgumentParser(description="Create a video with custom audio and subtitles.")
    parser.add_argument("video_path", help="Path to the input video file")
    parser.add_argument("audio_script_path", help="Path to the audio script text file")
    parser.add_argument("bg_music_path", help="Path to the background music file")
    parser.add_argument("subtitles_path", help="Path to the subtitles text file")
    parser.add_argument("output_path", help="Path for the output video file")

    args = parser.parse_args()

    create_video(args.video_path, args.audio_script_path, args.bg_music_path, args.subtitles_path, args.output_path)

if __name__ == "__main__":
    main()