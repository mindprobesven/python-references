# pip install playsound
# sudo apt-get install gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools python3-gst-1.0 python3-gi gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0
# pip install vext.gi

import sys
import time
from playsound import playsound

if __name__ == "__main__":
    try:
        print("Before playing sound")
        playsound('/home/ubuntu/Desktop/clearly.mp3')
        print("After playing sound")
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
