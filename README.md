# AutiCalm Audio Behavior Monitor

AutiCalm is a smart audio analysis tool designed to assist with autism support by detecting signs of distress such as echolalia (repetitive speech) and yelling. It uses machine learning and audio processing to provide real-time insights from raw `.wav` audio input.

> This project was developed for Hack404 to promote neurodiverse-friendly technology through compassionate, ML-powered solutions.

## Features

- Speech-to-Text: Uses OpenAI's Whisper pretrained model to transcribe speech from `.wav` files.
- Echolalia Detection: Identifies repeated words or phrases that may indicate distress.
- Yelling Detection: Analyzes volume level and flags when yelling is detected.
- Summarized Reports: Outputs clear feedback on detected audio behavior.

## Getting Started

### Requirements

- `Python 3.8+`
- Dependencies:
  - `openai-whisper`
  - `librosa`
  - `numpy`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Input Format

Add your input audio as `audio.wav`. Mono or stereo `.wav` files under 30 seconds are recommended.

## Usage

Run the script:

```bash
python AutiCalm.py
```

The script will:

- Transcribe the audio using Whisper

- Identify repeated words (echolalia)

- Detect yelling based on volume thresholds

- Display a summary report

## Project Structure
```bash
Hack404/
├── detect_behavior.py     # Main script
├── audio.wav              # Input audio file
├── README.md              # Project description
```

## Technical Overview

- Whisper: Provides high-accuracy transcription for natural and non-standard speech.

- Librosa: Used to extract audio features such as RMS and decibel levels for volume analysis.

- Natural Language Processing: Simple token analysis and frequency counting for echolalia detection.

## Use Cases
- Autism companion apps (e.g., AutiCalm)

- Behavioral monitoring tools for parents or therapists

- Classroom observation tools

- Accessible technology for neurodivergent individuals

## License
This project is licensed under the **MIT License**.

## Author
Created by Anish Paleja for Hack404

GitHub: https://github.com/anipaleja


