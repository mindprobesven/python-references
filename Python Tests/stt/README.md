SpeechRecognition installation
-------------------------------------------------------------

1. Install PIP packages
pip install SpeechRecognition

2. Install system site packages
sudo apt-get install flac                   # For recognize_google() install FLAC

3. Enable microphone recording
sudo apt-get install python3-pyaudio libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio

PocketSphinx installation
-------------------------------------------------------------

1. Install system site packages
sudo apt-get install swig

2. Install PIP packages
pip install pocketsphinx