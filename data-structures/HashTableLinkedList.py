# Given the list of names, we produce a hash code for each name
# and then using linked list method we put it into
# appropriate place in the array (creating HashMap effectively)
class HashTableLinkedList:
    def __init__(self, size):
        self.size = size
        self.list = [[]] * size

    def hash(self, name):
        index = ord(name[0]) % self.size
        return index

    def add(self, name):
        ind = self.hash(name)
        self.list[ind].append(name)

    def contains(self, name):
        ind = self.hash(name)
        if name in self.list[ind]:
            return True
        else:
            return False

    def remove(self, name):
        ind = self.hash(name)
        self.list[ind].remove(name)


if __name__ == "__main__":
    template = ["Smith", "James", "Jordan", "Georgeson",
                "Mahrez", "Nowak", "Vikiya", "Malos", "Nickson", "Baynes"]
    size = len(template)
    x = HashTableLinkedList(size)
    for name in template:
        x.add(name)
    print(x.contains("Adam"))
    print(x.contains("James"))
    print(x.contains("Jordan"))
    x.remove("Jordan")
    print(x.contains("Jordan"))
