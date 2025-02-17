class Stack:
    def __init__(self):
        self.item=[]
    def push(self, item):
        self.item.append(item)
    def pop(self):
        if self.item!=[]:
            return self.item.pop()
        else:
            return None

n=int(input())
l=list(map(int, input().split()))
stack=Stack()
current=0
ok=True
for i in l:
    popitem=stack.pop()
    if i==popitem:
        continue
    elif i>current:
        stack.push(popitem)
        for j in range(current+1, i+1):
            stack.push(j)
        current=i
        stack.pop()
    else:
        ok=False
        break
print('Yes' if ok else 'No')