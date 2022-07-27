from pynput import keyboard
import pyautogui as pg
import time


def antiafk_on(key):
    print(f'{key} released')
    if key == keyboard.Key.left:
        pg.keyDown('N')
        pg.keyDown('M')
    elif key == keyboard.Key.right:
        pg.press('N')
        pg.press('M')
    elif key == keyboard.Key.page_down:
        return False

with keyboard.Listener(on_release=antiafk_on) as listener:
    listener.join()
