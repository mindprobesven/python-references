playsound Installation - Ubuntu 19.1 / Raspberry Pi 3 B+
-------------------------------------------------------------

Play audio files (MP3, etc.) via Gstreamer in Python 3

1. Install system site packages
sudo apt-get install gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools python3-gst-1.0 python3-gi gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0

2. Install PIP packages
pip install playsound vext.gi
