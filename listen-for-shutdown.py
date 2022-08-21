#!/usr/bin/env python3
# use howchoo shutdown script. install the script which launch this one in /etc/init.d
# install gpiozero with sudo apt install python3-gpiozero
# put this script in /usr/local/bin/listen-for-shutdown.py


from gpiozero import Button
import subprocess
import time

def longpress():
    subprocess.call(['shutdown', '-h', 'now'], shell=False)

button = Button(3, hold_time=2)
button.when_held = longpress

while 1:
    time.sleep(1)
