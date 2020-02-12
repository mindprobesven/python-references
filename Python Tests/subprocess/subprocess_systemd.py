#!/usr/bin/env python3

import sys
import subprocess
from subprocess import Popen

def main():
    status_before = Popen(['systemctl', '--user', 'status', 'pulseaudio.service'], stdout=subprocess.PIPE).communicate()[0]
    print(status_before.decode("UTF-8"))

    Popen(['systemctl', '--user', 'restart', 'pulseaudio.service']).communicate()

    status_after = Popen(['systemctl', '--user', 'status', 'pulseaudio.service'], stdout=subprocess.PIPE).communicate()[0]
    print(status_after.decode("UTF-8"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
