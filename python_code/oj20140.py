s=input()
stack=[]
ans=''
i=0
while i<len(s):
    if ord('0')<=ord(s[i])<=ord('9'):
        j=i
        while ord('0')<=ord(s[j])<=ord('9'):
            j+=1
        stack.append(int(s[i:j]))
        i=j
    elif ord('a')<=ord(s[i])<=ord('z'):
        stack.append(s[i])
        i+=1
    elif s[i]==']':
        i+=1
        temp=''
        while stack and isinstance(stack[-1], str):
            temp=stack.pop()+temp
        if stack:
            temp=temp*stack.pop()
            stack.append(temp)
    else:
        i+=1
for j in stack:
    ans+=j
print(ans)
