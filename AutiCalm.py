import whisper
import librosa
import numpy as np
from collections import Counter


AUDIO_PATH = "PATH/TO/YOUR/FILE.wav"  # **Replace with your audio file path**
REPETITION_THRESHOLD = 3  # Number of times a word must repeat to be flagged
YELLING_VOLUME_DB = -20   # Volume (dB) threshold for yelling

print("Transcribing audio...")
model = whisper.load_model("base")
result = model.transcribe(AUDIO_PATH)
text = result["text"]
print("Transcription:", text)

def detect_repetition(transcript, threshold):
    words = transcript.lower().split()
    counts = Counter(words)
    repeated = {word: count for word, count in counts.items() if count >= threshold}
    return repeated

repeated_words = detect_repetition(text, REPETITION_THRESHOLD)
print("Repeated Words (Echolalia):", repeated_words)

def detect_yelling(audio_path, volume_threshold_db):
    y, sr = librosa.load(audio_path)
    rms = librosa.feature.rms(y=y)[0]
    avg_db = librosa.amplitude_to_db([np.mean(rms)])[0]
    print(f"Average Volume: {avg_db:.2f} dB")
    return avg_db > volume_threshold_db

yelling_detected = detect_yelling(AUDIO_PATH, YELLING_VOLUME_DB)
if yelling_detected:
    print("Yelling Detected")
else:
    print("No yelling detected")

print("\n--- Summary ---")
if repeated_words:
    print("Echolalia detected:", repeated_words)
else:
    print("No significant repetition detected.")

print("Yelling:", "Yes" if yelling_detected else "No")
