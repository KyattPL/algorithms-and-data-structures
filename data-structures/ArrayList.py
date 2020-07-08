# I mean there's no such thing as an array in Python so it's a bit redundant
# but still shows the concept of it.
class ArrayList:
    def __init__(self):
        self.min_capacity = 10
        self.size = 0
        self.array = []

    def push(self, value):
        if len(self.array) >= self.min_capacity:
            newList = self.array.append(value)
            self.array = newList
            self.size += 1
        else:
            self.array.append(value)
            self.size += 1

    def pop(self):
        self.size -= 1
        return self.array.pop()

    def add(self, value, index):
        self.size += 1
        if index == 0:
            newTab = [value]
            for elem in range(len(self.array) - 1):
                newTab.append(self.array.pop())
            self.array = newTab
        else:
            leftPart = self.array[:index]
            leftPart.append(value)
            rightPart = self.array[index:]
            for elem in range(len(rightPart)):
                leftPart.append(rightPart.pop(0))
            self.array = leftPart

    def remove(self, index):
        self.size -= 1
        if index == 0:
            self.array = self.array[1:]
        else:
            leftPart = self.array[:index]
            rightPart = self.array[index+1:]
            for elem in range(len(rightPart)):
                leftPart.append(rightPart.pop(0))
            self.array = leftPart

    def print_list(self):
        for elem in self.array:
            print(elem)

    def length(self):
        return self.size

    def contains(self, value):
        for elem in self.array:
            if elem == value:
                return True
        return False


if __name__ == "__main__":
    x = ArrayList()
    x.push(5)
    x.push(69)
    x.push(1337)
    x.print_list()
    x.remove(1)
    x.print_list()
    x.add(420, 1)
    x.print_list()
    print(x.length())
    print(x.contains(1337))
