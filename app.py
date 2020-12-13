import tkinter as tk


from anki_card import AnkiCard
from bag import Bag
import text_capture
from mouse_handler import MouseHandler

class App(tk.Tk):
    def __init__(self, bag):
        tk.Tk.__init__(self)
        self.title('Wordbag v0.1')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self._bag = bag
        self._handler = MouseHandler()
        self.labels = []
        self.entries = []
        self.button = tk.Button(self, text='Save')
        self.refresh_words()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.after(50, self.handler_loop)

    @property
    def bag(self):
        return self._bag

    def refresh_words(self):
        for label in self.labels:
            label.pack_forget()
        for entry in self.entries:
            entry.pack_forget()
        self.button.pack_forget()
        self.labels = []
        self.entries = []
        for i, card in enumerate(self.bag.elements):
            label = tk.Label(self, text=card.front, relief=tk.RIDGE, width = 20)
            label.grid(column=0, row=i)
            entry = tk.Entry(self, width = 20, relief=tk.RIDGE)
            entry.insert(0, card.back)
            entry.grid(column=1, row=i)
            self.labels.append(label)
            self.entries.append(entry)
        self.button = tk.Button(self, text='Save', width = 40, command=self.persist_bag)
        self.button.grid(row=len(self.bag.elements), columnspan=2)

    def persist_bag(self):
        self.bag.elements.clear()
        for i in range(len(self.entries)):
            front = self.labels[i]['text']
            back = self.entries[i].get()
            card = AnkiCard(front=front, back=back)
            self.bag.elements.add(card)
        self.bag.marshall(self.bag.filename)


    def on_closing(self):
        self.destroy()

    def handler_loop(self):
        if self.bag.file_changed():
            self._bag = Bag.from_file_or_new(f"{self.bag.name}.bag")
            self.refresh_words()

        self.after(500, self.handler_loop)

    