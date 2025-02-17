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

from itertools import permutations

n=int(input())
numlist=[i for i in range(1, n+1)]
permutation=list(permutations(numlist))

def avail(l):
    stack = Stack()
    current = 0
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
            return False
    return True

for l in permutation:
    if avail(l):
        print(*l)
