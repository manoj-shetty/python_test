from pynput.mouse import Listener
import pyautogui

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        if "right" in str(button):
            print("Right Clicked")
            pyautogui.click(button='right')
        else:
            print("Left Clicked")

with Listener(on_click=on_click) as listener:
    listener.join()