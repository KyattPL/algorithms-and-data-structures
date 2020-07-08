# Priority queue implemented using heap structure
class PriorityQueue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)
        self.swim(len(self.list) - 1)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return None
        retVal = self.list[0]
        if len(self.list) > 1:
            self.list[0] = self.list[len(self.list) - 1]
            self.sink(0)
        self.list.pop()
        return retVal

    def swap(self, index1, index2):
        temp = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = temp

    def swim(self, index):
        parent = (index - 1) // 2
        while index != 0 and self.list[index] > self.list[parent]:
            self.swap(index, parent)
            index = parent

    def sink(self, index):
        isDone = False
        child = 2*index + 1
        while not isDone and child < len(self.list):
            if child < (len(self.list) - 1) and self.list[child] < self.list[child+1]:
                child += 1
            if self.list[index] < self.list[child]:
                self.swap(index, child)
            else:
                isDone = True
            child = 2*index + 1


if __name__ == "__main__":
    x = PriorityQueue()
    x.enqueue(10)
    x.enqueue(423)
    x.enqueue(53)
    x.enqueue(298)
    x.enqueue(27)
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
