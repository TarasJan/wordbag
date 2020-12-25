import os
import time
import keyboard

if os.name == 'nt':
    import win32ui
    import win32clipboard

def capture_text():
    if os.name == 'nt':
        wnd = win32ui.GetForegroundWindow()
        print(wnd.GetWindowText())
        return get_clipboard()
    else:
        print('Unsupported OS')

def copy_paste():
    keyboard.press('ctrl+c')
    time.sleep(0.2)
    print('OK')
    keyboard.release('ctrl+c')
    time.sleep(0.1)

def get_clipboard():
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    print(data)
    win32clipboard.CloseClipboard()
    return data