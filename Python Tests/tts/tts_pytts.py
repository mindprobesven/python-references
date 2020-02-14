#!/usr/bin/env python3

import pyttsx3

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                          #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print(volume)                          #printing current volume level
engine.setProperty('volume', 0.25)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice

all_voices = ((str(voices.index(voice)), str(voice.id), str(voice.gender)) for voice in voices)
for voice in all_voices:
    print(": ".join(voice))

engine.setProperty('voice', voices[16].id)   # English British, male

engine.say("System diagnostics completed.")

engine.runAndWait()
engine.stop()
