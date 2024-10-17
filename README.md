# Video Creator

This project is a Python-based video creation tool that combines images, text, and audio to generate engaging video content.

## Files

- `video_creator.py`: Main script for creating videos
- `video_utils.py`: Utility functions for video creation
- `audio_script.txt`: Script for audio narration

## Features

- Combines multiple images into a video
- Adds text overlays to video frames
- Incorporates audio narration
- Customizable video duration and transitions

## Requirements

- Python 3.7+
- MoviePy
- Pillow (PIL)
- pyttsx3 (for text-to-speech, if used)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/video-creator.git
   cd video-creator
   ```

2. Install the required packages:
   ```
   pip install moviepy pillow pyttsx3
   ```

## Usage

1. Prepare your images and place them in an `images` directory.
2. Edit the `audio_script.txt` file with your narration script.
3. Run the video creator script:
   ```
   python video_creator.py
   ```

4. The generated video will be saved in the project directory.

## Customization

You can customize various aspects of the video creation process by modifying the parameters in `video_creator.py` and `video_utils.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
