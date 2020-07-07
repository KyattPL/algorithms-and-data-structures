# Since Python doesn't have a built-in array data structure
# I'm going to use a regural list with capacity (to make it interesting)
class Queue:
    def __init__(self, capacity=10):
        self.list = []
        self.capacity = capacity

    def enqueue(self, value):
        if len(self.list) != self.capacity:
            self.list.append(value)
            return True
        else:
            return "QueueOverflowException"

    def dequeue(self):
        if len(self.list) != 0:
            val = self.list.pop(0)
            return val
        else:
            return "IndexOutOfBoundsException"


if __name__ == "__main__":
    x = Queue(3)
    print(x.enqueue(10))
    print(x.enqueue(69))
    print(x.enqueue(2137))
    print(x.enqueue(423))
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
