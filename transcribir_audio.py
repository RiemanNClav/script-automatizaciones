import whisper

model = whisper.load_model('medium')
result = model.transcribe('angel_audio.mp3')

print(result['text'])