#!/usr/bin/env python3

import sys
import subprocess
from subprocess import Popen, PIPE

def main():
    # Run the command line with the arguments passed as a list of strings or by setting the shell argument to a True value
    subprocess.call(['df', '-h'])
    subprocess.call('du -hs $HOME', shell=True)

    # The underlying process creation and management in the subprocess module is handled by the Popen class
    p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
    # communicate() method executes the command and returns a tuple (stdoutdata, stderrdata)
    print(p.communicate())

    p1 = Popen(["dmesg"], stdout=PIPE)
    print(p1.communicate())

    ping = subprocess.Popen(['ping', '-c 2', 'www.google.com'], stdout=subprocess.PIPE).communicate()
    print(ping)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
