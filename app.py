import tkinter as tk
from tkinter.messagebox import showinfo

from anki import AnkiCard
from bag import Bag
import text_capture
from mouse_handler import MouseHandler

class App(tk.Tk):
    def __init__(self, bag):
        tk.Tk.__init__(self)
        self.title('Wordbag v0.1')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.initialize_menu()
        self._bag = bag
        self._handler = MouseHandler(self.insert_anki_card)
        self.labels = []
        self.entries = []
        self.button = tk.Button(self, text='Save')
        self.refresh_words()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.after(50, self.handler_loop)

    @property
    def bag(self):
        return self._bag

    def initialize_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        fileMenu = tk.Menu(menu)
        fileMenu.add_command(label="Open", command=self.load_bag)
        fileMenu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="File", menu=fileMenu)

        menu.add_command(label="About", command=self.show_info_box)

    def refresh_words(self):
        for label in self.labels:
            label.pack_forget()
        for entry in self.entries:
            entry.pack_forget()
        self.button.pack_forget()
        self.labels = []
        self.entries = []
        for i, card in enumerate(self.bag.elements):
            remove_button = tk.Button(self, text='x', command=self.on_remove_click(card))
            remove_button.grid(column=0, row=i)
            label = tk.Label(self, text=card.front, relief=tk.RIDGE, width = 20)
            label.grid(column=1, row=i)
            entry = tk.Entry(self, width = 20, relief=tk.RIDGE)
            entry.insert(0, card.back)
            entry.grid(column=2, row=i)
            self.labels.append(label)
            self.entries.append(entry)
        self.button = tk.Button(self, text='Save', width = 40, command=self.persist_bag)
        self.button.grid(row=len(self.bag.elements), columnspan=3)

    def persist_bag(self):
        self.bag.elements.clear()
        for i in range(len(self.entries)):
            front = self.labels[i]['text']
            back = self.entries[i].get()
            card = AnkiCard(front=front, back=back)
            self.bag.elements.add(card)
        self.bag.marshall()
        self.bag.dump_to_anki()

    def on_closing(self):
        self.destroy()

    def show_info_box(self):
        showinfo(
            title='Wordbag 0.1v', 
            message="Wordbag is a free Anki deck builder released under MIT license for sentence mining.\n Mine words from websites, documents and movie titles.\n 2020 @ jantaras.com"
        )

    def handler_loop(self):
        if self.bag.file_changed():
            self._bag = Bag.from_file_or_new(f"{self.bag.name}.bag")
            self.refresh_words()

        self.after(500, self.handler_loop)

    def anki_card_from_capture(self):
        captured_text = text_capture.capture_text()
        return AnkiCard(front=captured_text, back='')

    def insert_anki_card(self):
        new_card = self.anki_card_from_capture()
        print(new_card.front)
        self.bag.elements.add(new_card)
        self.bag.dump_to_file()
        self.bag.marshall()

    def on_remove_click(self, card):
        def on_click():
            self.bag.elements.remove(card)
            self.refresh_words()
        return on_click

    def load_bag(self):
        self._bag = Bag.from_file_or_new()
        self.refresh_words()
   