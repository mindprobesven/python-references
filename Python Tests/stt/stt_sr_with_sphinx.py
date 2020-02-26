#!/usr/bin/env python3

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    r.adjust_for_ambient_noise(source)

    print("Say something!")
    audio = r.listen(source)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio, keyword_entries=[('computer', 0.5)]))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
