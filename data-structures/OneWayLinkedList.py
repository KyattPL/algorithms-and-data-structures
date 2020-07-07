# With Head only
class OneWayLinkedList:
    class Element:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = self.Element(val)
        else:
            elem = self.head
            while elem.next != None:
                elem = elem.next
            elem.next = self.Element(val)

    def contains(self, val):
        elem = self.head
        while elem:
            if elem.value == val:
                return True
            elem = elem.next
        return False

    def print_list(self):
        elem = self.head
        while elem:
            print(elem.value)
            elem = elem.next

    def pop(self):
        elem = self.head
        while elem.next.next != None:
            elem = elem.next
        val = elem.next.value
        elem.next = None
        return val

    def length(self):
        count = 0
        elem = self.head
        if elem is None:
            return count
        else:
            while elem:
                elem = elem.next
                count += 1
        return count

    def remove(self, index):
        if index < 0 or index >= self.length():
            return None
        elem = self.head
        temp = 0
        ind = 1
        if index == 0 and self.head:
            temp = elem.value
            if elem.next:
                self.head = elem.next
                return temp
            else:
                self.head = None
                return temp
        else:
            temp = None
            while ind != index and elem:
                ind += 1
                elem = elem.next
            temp = elem.next.value
            elem.next = elem.next.next
            return temp

    def add(self, val, index):
        if index < 0 or self.length() <= index:
            return False
        elif index == 0:
            elem = self.head
            if elem is None:
                self.add(val)
            else:
                newElem = self.Element(val)
                newElem.next = elem
                self.head = newElem
        else:
            elem = self.head
            ind = 1
            while index != ind and elem:
                ind += 1
                elem = elem.next
            newElem = self.Element(val)
            if elem.next:
                newElem.next = elem.next
                elem.next = newElem
            else:
                newElem.next = None
                elem.next = newElem
        return True


if __name__ == "__main__":
    x = OneWayLinkedList()
    x.push(5)
    x.push(4)
    x.push(1337)
    x.push(69)
    temp = x.pop()
    x.print_list()
    print(x.contains(1337))
    x.remove(1)
    x.print_list()
    x.add(69, 0)
    x.print_list()
    x.add(12, 1)
    x.print_list()
