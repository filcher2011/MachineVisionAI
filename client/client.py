import time
import os

from tools.toolsForProgram import anim_text, color_text
import pickledb

db = pickledb.load('../ai/idcam.db', True)

def loaing():
    anim_text('Loading...\n', "green", 0.1)
    time.sleep(1)
    anim_text('Starting...\n', "green", 0.1)
    time.sleep(0.5)
    os.system('cls')
    greating()

def greating():
    anim_text('Machine Vision AI\n', "yellow", 0.2)
    print('Welcome to Machine Vision AI. This program contains a program that calculates the position of a person’s eyes and face on a camera or in a photo. Press enter to start programm')
    input("")
    os.system('cls')
    print('Pleasse enter your camera\' id')
    print(('By default, USB or built-in camera is under ID 0'))
    id = int(input())
    try:
        db.set('idcam', id)
        os.system('python ../ai/ai.py')
    except ValueError:
        pass

if __name__ == '__main__':
    loaing()
