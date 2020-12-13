import os
import time
from pynput.keyboard import Key, Controller

if os.name == 'nt':
    import win32ui
    import win32clipboard

def capture_text():
    if os.name == 'nt':
        wnd = win32ui.GetForegroundWindow()
        print(wnd.GetWindowText())
        copy_paste()
        return get_clipboard()
    else:
        print('Unsupported OS')

def copy_paste():
    keyboard = Controller()

    keyboard.press(Key.ctrl)
    keyboard.press('c')
    time.sleep(0.1)
    keyboard.release('c')
    print('OK')
    keyboard.release(Key.ctrl)

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    print(data)
    win32clipboard.CloseClipboard()
    return data