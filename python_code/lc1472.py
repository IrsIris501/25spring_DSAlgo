class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleListNode:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def print_list(self):
        pointer=self.head
        while pointer:
            print(pointer.val, end=' ')
            pointer=pointer.next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.items=DoubleListNode()
        self.items.append(homepage)
        self.pointer=self.items.head

    def visit(self, url: str) -> None:
        self.pointer.next=Node(url)
        tmp=self.pointer
        self.pointer=self.pointer.next
        self.pointer.prev=tmp

    def back(self, steps: int) -> str:
        count=steps
        while self.pointer.prev and count:
            self.pointer=self.pointer.prev
            count-=1
        return self.pointer.val

    def forward(self, steps: int) -> str:
        count=steps
        while self.pointer.next and count:
            self.pointer=self.pointer.next
            count-=1
        return self.pointer.val

homepage=input()
obj=BrowserHistory(homepage)
while True:
    a, b=input().split()
    if a=='v':
        obj.visit(b)
    elif a=='f':
        print(obj.forward(int(b)))
    else:
        print(obj.back(int(b)))
