#!/usr/bin/env python3

import pathlib
from watson_developer_cloud import TextToSpeechV1
from playsound import playsound

from config import Watson_Config

text_to_speech = TextToSpeechV1(iam_apikey=Watson_Config.IAM_APIKEY, url=Watson_Config.API_URL)

speech_data = text_to_speech.synthesize('System failing! I am about to crash. Sorry, I\'m an idiot!', accept='audio/mp3', voice='en-US_MichaelV3Voice').result.content

# print(speech_data)

with open('watson.mp3', 'wb') as audio_file:
    audio_file.write(speech_data)

audio_file_path = str(pathlib.Path(__file__).cwd().resolve() / 'watson.mp3').replace(' ', '%20')
print(audio_file_path)

print("Before playing sound")
playsound(audio_file_path)
print("After playing sound")
