#Tools for program by filcher2011
import termcolor
import time

def anim_text(text, color, speed=0.1):
    for c in text:
        print(termcolor.colored(c, color), end='', flush=True)
        time.sleep(speed)

def color_text(self, text: str, color: str) -> str:
    termcolor.colored(text, color)

