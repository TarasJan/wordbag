import pickle
import os.path

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
        return instance

    def __init__(self, name):
        self._name = name
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

    def __str__(self):
        return f"Bag {self.name}: <\n" + "\n".join(self.elements) + "\n>"