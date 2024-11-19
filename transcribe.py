import whisper

def transcribe_with_whisper(audio_file_path):
    model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
    result = model.transcribe(audio_file_path, language="ur")
    print("Transcript:", result['text'])
    return result['text']


transcript = transcribe_with_whisper("test_audio.wav")
print("Transcription Result:", transcript)
