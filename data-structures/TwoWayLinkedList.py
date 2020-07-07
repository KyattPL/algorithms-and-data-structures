# With Head and Tail
class TwoWayLinkedList:
    class Element:
        def __init__(self, val):
            self.value = val
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if self.head is None:
            newElem = self.Element(val)
            self.head = newElem
            self.tail = newElem
        else:
            newElem = self.Element(val)
            self.tail.next = newElem
            newElem.previous = self.tail
            self.tail = newElem

    def print_list(self):
        elem = self.head
        if elem is None:
            return
        else:
            while elem != self.tail:
                print(elem.value)
                elem = elem.next
            print(self.tail.value)

    def print_reverse(self):
        elem = self.tail
        if elem is None:
            return
        else:
            while elem != self.head:
                print(elem.value)
                elem = elem.previous
            print(self.head.value)

    def pop(self):
        elem = self.tail
        if elem is None:
            return None
        else:
            newTail = elem.previous
            val = elem.value
            self.tail = newTail
            return val

    def contains(self, val):
        elem = self.head
        if elem is None:
            return False
        else:
            while elem:
                if elem.value == val:
                    return True
                else:
                    elem = elem.next
            return False

    def length(self):
        count = 0
        elem = self.head
        if elem is None:
            return 0
        else:
            while elem:
                count += 1
                elem = elem.next
            return count

    def add(self, val, index):
        if index < 0 or index >= self.length():
            return None
        else:
            if index == 0:
                elem = self.head
                newElem = self.Element(val)
                newElem.next = elem
                elem.previous = newElem
                self.head = newElem
                return
            else:
                elem = self.head
                ind = 1
                while ind != index:
                    ind += 1
                    elem = elem.next
                newElem = self.Element(val)
                if elem.next:
                    newElem.next = elem.next
                    newElem.previous = elem
                    elem.next.previous = newElem
                    elem.next = newElem
                else:
                    newElem.next = None
                    newElem.previous = elem
                    elem.next = newElem

    def remove(self, index):
        if index < 0 or index >= self.length():
            return None
        else:
            if index == 0:
                elem = self.head
                val = elem.value
                self.head = elem.next
                if self.head is None:
                    self.tail = None
                return val
            else:
                elem = self.head
                ind = 0
                while ind != index:
                    ind += 1
                    elem = elem.next
                if self.tail != elem:
                    val = elem.value
                    elem.previous.next = elem.next
                    elem.next.previous = elem.previous
                    return val
                else:
                    val = elem.value
                    elem.previous.next = None
                    self.tail = elem.previous
                    return val


if __name__ == "__main__":
    x = TwoWayLinkedList()
    x.push(3)
    x.push(69)
    x.push(2137)
    print(x.contains(69))
    print(x.length())
    x.print_list()
    x.add(32, 1)
    x.print_list()
    x.remove(3)
    x.print_list()
