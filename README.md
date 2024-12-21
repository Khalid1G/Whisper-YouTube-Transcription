# YouTube Video Transcriber

A Python script that automatically downloads YouTube videos and generates text transcriptions using OpenAI's Whisper model.

## Features

- Downloads audio from YouTube videos using yt-dlp
- Transcribes audio using OpenAI's Whisper model
- Saves transcriptions as formatted text files
- Handles temporary file management
- Supports various audio formats through FFmpeg
- Processes transcriptions into readable sentences

## Prerequisites

Before running this script, make sure you have the following installed:

```bash
pip install -r requirements.txt
```

Required packages:

- yt-dlp
- whisper
- librosa
- ffmpeg (system dependency)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Khalid1G/Whisper-YouTube-Transcription.git
cd Whisper-YouTube-Transcription
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Install FFmpeg (if not already installed):

- On Ubuntu/Debian: `sudo apt-get install ffmpeg`
- On macOS: `brew install ffmpeg`
- On Windows: Download from [FFmpeg official website](https://ffmpeg.org/download.html)

## Usage

1. Run the script:

```bash
python transcriber.py
```

2. Enter the YouTube video ID when prompted. The video ID is the part after `v=` in the YouTube URL.
   For example, for `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the ID is `dQw4w9WgXcQ`

3. The script will:
   - Download the audio from the YouTube video
   - Process the audio using Whisper
   - Save the transcription to `Youtube/[video_id]_transcription.txt`

## Output

The transcription will be saved in the `Youtube` directory with the filename pattern:
`[video_id]_transcription.txt`

The output text is formatted with one sentence per line for better readability.

## Project Structure

```
.
├── transcriber.py          # Main script
├── yt_transcription.ipynb  # Notebook script
├── requirements.txt        # Python dependencies
├── Youtube/                # Directory for transcription outputs
└── README.md               # This file
```

## Performance

- Transcription time varies based on:
  - Video length
  - Computer specifications
  - Chosen Whisper model ("base" in this implementation)

## Limitations

- Requires stable internet connection for YouTube downloads
- Processing time depends on video length and hardware capabilities
- Accuracy depends on audio quality and Whisper model used

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

[MIT License](./LICENSE)

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
