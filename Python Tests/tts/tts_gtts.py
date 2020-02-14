#!/usr/bin/env python3

import pathlib
from gtts import gTTS
from playsound import playsound

audio_file_path = str(pathlib.Path(__file__).cwd().resolve() / 'audio1.mp3')
print(audio_file_path)

tts = gTTS(text='System diagnostics completed!', tld='com', lang='en', lang_check=False)
tts.save("audio1.mp3")

print("Before playing sound")
playsound(audio_file_path)
print("After playing sound")
