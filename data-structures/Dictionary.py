# Based on list
class Dictionary:
    def __init__(self):
        self.dictionary = []

    def add(self, key, value):
        self.dictionary.append((key, value))

    def get(self, key):
        for elem in self.dictionary:
            if elem[0] == key:
                return elem[1]
        return None

    def remove(self, key):
        for (index, value) in enumerate(self.dictionary):
            if value[0] == key:
                break
        return self.dictionary.pop(index)

    def keys(self):
        temp = []
        for elem in self.dictionary:
            temp.append(elem[0])
        return temp

    def values(self):
        temp = []
        for elem in self.dictionary:
            temp.append(elem[1])
        return temp


if __name__ == "__main__":
    x = Dictionary()
    x.add("Polish", 1)
    x.add("English", 2)
    x.add("German", 3)
    print(x.keys())
    print(x.values())
