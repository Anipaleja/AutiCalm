# AutiCalm Audio Behavior Monitor

AutiCalm is a smart audio analysis tool designed to assist with autism support by detecting signs of distress such as echolalia (repetitive speech) and yelling. It uses machine learning and audio processing to provide real-time insights from raw `.wav` audio input.

This project was developed for Hack404 to promote neurodiverse-friendly technology through compassionate, ML-powered solutions.

## Features

- Speech-to-Text: Uses OpenAI's Whisper to transcribe speech from `.wav` files.
- Echolalia Detection: Identifies repeated words or phrases that may indicate distress.
- Yelling Detection: Analyzes volume level and flags when yelling is detected.
- Summarized Reports: Outputs clear feedback on detected audio behavior.

## Getting Started

### Requirements

- Python 3.8+
- Dependencies:
  - `openai-whisper`
  - `librosa`
  - `numpy`

Install dependencies:

```bash
pip install -r requirements.txt
```
