import speech_recognition as sr
AUDIO_FILE = 'voice1.wav'

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
print('\n音声データの文字起こし結果：\n\n', r.recognize_google(audio, language='ja'))
