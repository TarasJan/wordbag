import threading
from pynput import mouse

class MouseHandler:
    def __init__(self):
        self._listener = mouse_listener(self.on_click())
        self._click_buffer = 0

    @property
    def listener(self):
        return self._listener

    def on_click(self):
        def on_klik(x, y, button, pressed):
            log_click(x, y, button, pressed)
            if not pressed and button == mouse.Button.right:
                return self.register_button_release()
            else:
                return True
        return on_klik

    def register_button_release(self):
        self._click_buffer +=1
        self.schedule_buffer_clearing()
        print(f"Release count {self._click_buffer}")
        if self._click_buffer >= 3:  
            self._buffer_timer.cancel()  
            return False
        else:
            return True

    def schedule_buffer_clearing(self):
        if self._click_buffer == 1:
            self._buffer_timer = threading.Timer(1.5, self.clear_click_buffer)
            self._buffer_timer.start()
    
    def clear_click_buffer(self):
        print('Clearing click buffer')
        self._click_buffer = 0

def log_click(x, y, button, pressed):
    button_name = 'RMB' if button == mouse.Button.right else 'LMB'
    action_name = 'Pressed' if pressed else 'Released'
    print('{0} {1} at {2}'.format(action_name, button_name, (x, y)))

def mouse_listener(on_click):
    return mouse.Listener(
        on_click=on_click
    )