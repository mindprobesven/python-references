#!/usr/bin/env python3

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

# print(sr.Microphone.list_microphone_names())

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

text = r.recognize_google(audio, show_all=True)
print(text)
