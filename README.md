# Video media Creator 

## Project Background

Due to the lack of flexibility in current end-to-end video generation systems and their limitations in real-world applications, we developed this project to enable fine-grained control over multimedia content generation through text, images, and audio. The project addresses the following key challenges:

- Insufficient detailed control in existing end-to-end video generation models
- Difficulties in ensuring quality and coherence of generated content
- Lack of precise synchronization control between text, images, and audio
- Limited application scenarios that fail to meet actual business requirements

This project is submitted as part of Ready Tensor's Computer Vision Projects Expo 2024. It demonstrates an innovative approach to automated video content creation by combining computer vision, text processing, and audio synthesis.

## Project Overview

This Python-based video creation tool leverages computer vision and AI to automatically generate engaging video content by intelligently combining images, text, and audio narration.
examples:
input_video:
![input_video](input_video.mp4)
output_video:
![output_video](output_video.mp4)
## Features

- Automated video composition from image sequences
- Intelligent text overlay positioning using computer vision
- Dynamic audio-visual synchronization
- Smart transition effects based on content analysis
- Customizable video duration and style parameters
- Automated audio features:
  - AI-powered subtitle generation and synchronization
  - Text-to-speech narration with natural voice
  - AI-generated background music using OpenMusic models
  - Intelligent background music selection and mixing
  - Audio level balancing between speech and music
  - Multi-language subtitle support

## Technical Implementation

- Computer Vision algorithms for image analysis and composition
- Text positioning optimization using visual saliency detection
- Audio-visual synchronization through content-aware timing
- Modular architecture for easy extension and customization
- Audio processing capabilities:
  - Speech recognition for automatic subtitle generation
  - Advanced TTS (Text-to-Speech) integration
  - Dynamic audio mixing and normalization
  - AI background music generation using HuggingFace's OpenMusic models
  - Music tempo and mood analysis for scene matching

## Requirements

- Python 3.7+
- MoviePy
- edge-tts
- OpenMusic (via Hugging Face)
- FFmpeg (for advanced audio processing)

## Background Music Generation

The project uses [HuggingFace's OpenMusic](https://huggingface.co/openmusic) for AI-powered background music generation. This feature allows:


To use the OpenMusic BGM generation:

1. Access the OpenMusic models through Hugging Face
2. Select appropriate music datasets (e.g., openmusic/cc0-1.0-music for royalty-free music)
3. Generate background music that matches your video's mood and tempo

## Video Generation

### Raw Video Generation
The project uses [Vchitect-2.0](https://github.com/Vchitect/Vchitect-2.0), a state-of-the-art video diffusion model, for generating the initial video content. Features include:

- Text-to-video generation with high quality and coherence
- Support for resolutions up to 720x480 at 8fps
- Customizable generation parameters:
  - Number of inference steps (default: 100)
  - Guidance scale (default: 7.5)
  - Video dimensions and frame count
  - Custom prompts for precise content control

#### Installation Requirements for Vchitect-2.0:
```bash
conda create -n VchitectXL -y
conda activate VchitectXL
conda install python=3.11 pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia -y
pip install -r requirements.txt
```

#### Usage with Vchitect-2.0:
```bash
python inference.py --test_file assets/test.txt --save_dir "${save_dir}" --ckpt_path "${ckpt_path}"
```

The generated raw videos can then be enhanced with:
- Resolution upscaling to 2K
- Frame rate interpolation to 24fps
- Additional effects and transitions
- Audio synchronization
  
## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/video-creator.git
   cd video-creator
   ```

2. Install the required packages:
   ```
   pip install moviepy pillow pyttsx3 opencv-python
   ```

## Usage

The script can be run from the command line with the following arguments:

```bash
python video_creator.py <video_path> <audio_script_path> <bg_music_path> <subtitles_path> <output_path>
```

Arguments:
- `video_path`: Path to input video file
- `audio_script_path`: Path to audio script text file
- `bg_music_path`: Path to background music file
- `subtitles_path`: Path to subtitles file
- `output_path`: Path for output video file

Example:
```bash
python video_creator.py input_video.mp4 audio_script.txt background_music.wav audio_script.txt output_video.mp4
```

For help on usage:
```bash
python video_creator.py --help
```

### File Requirements

Before running the script, ensure you have:
1. Input video file (mp4 format recommended)
2. Audio script text file containing the narration
3. Background music file (wav format recommended)
4. Subtitles file in text format
5. Write permissions for the output directory

The script will validate all input files and create the output directory if it doesn't exist.

## Project Structure

- `video_creator.py`: Main script for video generation
- `video_utils.py`: Utility functions and CV algorithms
- `audio_script.txt`: Narration script template

## Future Enhancements（todo）

- Deep learning-based image selection and ordering
- Real-time preview capabilities
- Advanced visual effect generation
- Multi-language supporttodo
- Cloud-based processing options

## Contributing

We welcome contributions! Please feel free to submit Pull Requests or open issues for discussion.

## Competition Details

This project is part of Ready Tensor's Computer Vision Projects Expo 2024, showcasing innovative applications of computer vision and multi-modal AI technologies.

## License

This project is open source and available under the [MIT License](LICENSE).



## Tags / Keywords

### Core Technologies
- `#ComputerVision`
- `#AI`
- `#VideoGeneration`
- `#TextToVideo`
- `#TextToSpeech`
- `#DeepLearning`

### Features
- `#VideoProcessing`
- `#AudioSynthesis`
- `#SubtitleGeneration`
- `#BackgroundMusicGeneration`
- `#MultiModalAI`

### Frameworks & Tools
- `#Vchitect`
- `#OpenMusic`
- `#EdgeTTS`
- `#MoviePy`
- `#PyTorch`

### Applications
- `#ContentCreation`
- `#MediaProduction`
- `#AutomatedVideoEditing`
- `#AIAssistant`
- `#CreativeAI`


