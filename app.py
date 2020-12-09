import tkinter as tk

from bag import Bag
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
        self.destroy()

    def handler_loop(self):
        self._bag = Bag.from_file_or_new(f"{self.bag.name}.bag")
        self.refresh_words()

        self.after(500, self.handler_loop)

    