import threading
import mouse

class MouseHandler:
    def __init__(self, insertion_callback):
        self._callback = insertion_callback
        mouse.on_right_click(self.register_button_release)
        self._click_buffer = 0

    def reset_listener(self):
        self._click_buffer = 0

    def register_button_release(self):
        self._click_buffer +=1
        self.schedule_buffer_clearing()
        print(f"Release count {self._click_buffer}")
        if self._click_buffer >= 4:
            self._callback()
            self._buffer_timer.cancel()
            self.clear_click_buffer()

    def schedule_buffer_clearing(self):
        if self._click_buffer == 1:
            self._buffer_timer = threading.Timer(1.5, self.clear_click_buffer)
            self._buffer_timer.start()
    
    def clear_click_buffer(self):
        print('Clearing click buffer')
        self._click_buffer = 0

# def log_click(x, y, button, pressed):
#     button_name = 'RMB' if button == mouse.Button.right else 'LMB'
#     action_name = 'Pressed' if pressed else 'Released'
#     print('{0} {1} at {2}'.format(action_name, button_name, (x, y)))
