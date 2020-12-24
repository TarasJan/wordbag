import pickle
import os.path
import time
from tkinter.filedialog import askopenfilename

import genanki
from anki import AnkiModel 

class Bag:
    @classmethod
    def from_file_or_new(cls, filename=None):
        if filename is None:
            selected_filename = askopenfilename()
            return Bag.from_file_or_new(selected_filename)
        elif os.path.isfile(filename):
            print(f"Unmarshalling from file: {filename}")
            return Bag.from_file(filename)
        else:
            return Bag(filename.split('.')[0])

    @classmethod
    def from_file(_cls, filename):
        with open(filename, 'rb') as file:
            instance = pickle.load(file)
            instance.filename = filename
            instance.timestamp = time.ctime(os.path.getmtime(instance.filename))
        return instance

    def __init__(self, name):
        self._name = name
        self.timestamp = 0
        self.filename = f"{self.name}.bag"
        self._elements = set()

    @property
    def name(self):
        return self._name

    @property
    def elements(self):
        return self._elements

    def marshall(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    def dump_to_file(self):
        with open(f"{self.filename}.txt", 'w', encoding='utf-8') as file:
            file.write(f"Bag {self.name}:\n") 
            file.writelines(self.elements.__str__())

    def dump_to_anki(self):
        my_deck = genanki.Deck(
        2059400110,
        self.name)
        for element in self.elements:
            my_deck.add_note(
                genanki.Note(
                model=AnkiModel,
                fields=[element.front, element.back]
                )
            )

        genanki.Package(my_deck).write_to_file(f"{self.filename}.apkg")


    def file_changed(self):
        try:
            return self.timestamp != time.ctime(os.path.getmtime(self.filename))
        except FileNotFoundError:
            return True

    def __str__(self):
        return f"Bag {self.name}: <\n" + "\n".join(self.elements) + "\n>"