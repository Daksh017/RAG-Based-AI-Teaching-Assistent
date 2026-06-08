import whisper
model = whisper.load_model("large-v2")

result = model.transcribe("audios/1_Intro_And_Installationof_SQL.mp3", language="Hindi", task="translate")
print(result["text"])