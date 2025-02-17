class Stack:
    def __init__(self):
        self.item=[]
    def push(self, item):
        self.item.append(item)
    def pop(self):
        if self.item:
            return self.item.pop()
        else:
            return None

while True:
    try:
        s=input()
    except:
        break
    print(s)
    stack_left=Stack()
    stack_right=Stack()
    for i in range(len(s)):
        if s[i]=='(':
            stack_left.push(i)
        elif s[i]==')':
            if stack_left.item:
                stack_left.pop()
            else:
                stack_right.push(i)
    output=[' ' for i in range(len(s))]
    for i in stack_right.item:
        output[i]='?'
    for i in stack_left.item:
        output[i]='$'
    outstr=''
    for i in output:
        outstr+=i
    print(outstr)

