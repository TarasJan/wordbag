import pickle
import os.path
import time

class Bag:
    @classmethod
    def from_file_or_new(cls, filename):
        if os.path.isfile(filename):
            print(f"Unmarshalling from file: {filename}")
            return Bag.from_file(filename)
        else:
            return Bag(filename.split('.')[0])

    @classmethod
    def from_file(_cls, filename):
        with open(filename, 'rb') as file:
            instance = pickle.load(file)
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

    def marshall(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def dump_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Bag {self.name}:\n") 
            file.writelines(self.elements.__str__())

    def file_changed(self):
        try:
            return self.timestamp != time.ctime(os.path.getmtime(self.filename))
        except FileNotFoundError:
            return True

    def __str__(self):
        return f"Bag {self.name}: <\n" + "\n".join(self.elements) + "\n>"