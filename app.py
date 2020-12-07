import tkinter as tk

import text_capture
from mouse_handler import MouseHandler

class App(tk.Tk):
    def __init__(self, bag):
        tk.Tk.__init__(self)
        self._bag = bag
        self._handler = MouseHandler()
        self.label = tk.Label(self, text=self.bag)
        self.refresh_words()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.after(50, self.handler_loop)

    @property
    def bag(self):
        return self._bag

    def refresh_words(self):
        self.label.config(text = self.bag)
        self.label.pack()

    def on_closing(self):
        self.bag.dump_to_file('result.txt')
        self.bag.marshall('phrases.bag')
        self.destroy()

    def handler_loop(self):
        if not self._handler.listener.is_alive():
            captured_text = text_capture.capture_text()
            self.bag.elements.append(captured_text)
            self.refresh_words()
            self._handler.reset_listener()

        self.after(50, self.handler_loop)

    