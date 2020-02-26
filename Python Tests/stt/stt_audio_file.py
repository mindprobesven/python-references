#!/usr/bin/env python3

import speech_recognition as sr

r = sr.Recognizer()
audio_data = sr.AudioFile('new-mic-test.wav')
with audio_data as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)

# text = r.recognize_google(audio, show_all=True)
text = r.recognize_google(audio)
print(text)
