# Since Python doesn't have a built-in array data structure
# I'm going to use a regural list with capacity (to make it interesting)
class Stack:
    def __init__(self, capacity=10):
        self.list = []
        self.capacity = capacity

    def push(self, val):
        if len(self.list) != self.capacity:
            self.list.append(val)
            return True
        else:
            return "StackOverflowException"

    def pop(self):
        if len(self.list) != 0:
            val = self.list.pop()
            return val
        else:
            return "IndexOutOfBoundsException"


if __name__ == "__main__":
    x = Stack(3)
    print(x.push(10))
    print(x.push(69))
    print(x.push(2137))
    print(x.push(423))
    print(x.pop())
    print(x.pop())
    print(x.pop())
    print(x.pop())
