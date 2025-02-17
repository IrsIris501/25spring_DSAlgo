class Stack:
    def __init__(self):
        self.item=[]
    def push(self, item):
        self.item.append(item)
    def pop(self):
        if self.item!=[]:
            return self.item.pop()
        else:
            return -1

stack=Stack()
n=int(input())
for i in range(n):
    s=input()
    if s[1]=='o':
        print(stack.pop())
    else:
        stack.push(int(s[5::]))
