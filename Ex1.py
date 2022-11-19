class List:
    Header = None

    def Add(self, data):
        if self.Header == None:
            self.Header = Node(data)
        else:
            self.Header.Add(data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def setPrev(self, prev):
        self.prev = prev

    def setNext(self, next):
        self.next = next

    def Add(self, data):
        if self.next == None:
            self.next = Node(data)
            self.next.setPrev(self)
        else:
            self.next.Add(data)

    def Print(self):
        print(f"Data: {self.data}")
        if self.prev != None:
            print(f"Prev Data: {self.prev.data}")
        if self.next != None:
            print(f"Next Data: {self.next.data}")
        print()
        if self.next != None:
            self.next.Print()


LinkList = List()
LinkList.Add(1)
LinkList.Add(2)
LinkList.Add(3)
LinkList.Add(4)
LinkList.Header.Print()