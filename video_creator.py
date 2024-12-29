import argparse
import os
from video_utils import create_video

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create a video with audio and subtitles')
    parser.add_argument('video_path', help='Path to input video file')
    parser.add_argument('audio_script_path', help='Path to audio script text file')
    parser.add_argument('bg_music_path', help='Path to background music file')
    parser.add_argument('subtitles_path', help='Path to subtitles file')
    parser.add_argument('output_path', help='Path for output video file')
    return parser.parse_args()

def validate_files(args):
    # Check if input files exist
    for path, name in [
        (args.video_path, 'Input video'),
        (args.audio_script_path, 'Audio script'),
        (args.bg_music_path, 'Background music'),
        (args.subtitles_path, 'Subtitles')
    ]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"{name} file not found: {path}")
    
    # Check if output directory exists
    output_dir = os.path.dirname(args.output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

def main():
    args = parse_arguments()
    try:
        validate_files(args)
        create_video(
            args.video_path,
            args.audio_script_path,
            args.bg_music_path,
            args.subtitles_path,
            args.output_path
        )
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())