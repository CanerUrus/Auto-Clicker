import pyautogui
from pynput.keyboard import *

delay =60
trigger_key = KeyCode.from_char('z')
exit_key =Key.f1
paused = True
running = True

def on_press(key):
    global paused, running
    if key==trigger_key:
        if paused:
            paused=False
        else:
            paused= True
    elif key == exit_key:
        running = False

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    while running:
        if not paused:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()

if __name__== "__main__":
    main()
