s=input().split()
i=0
while i<len(s):
    if s[i]=='+' or s[i]=='-':
        s[i], s[i+1]=s[i+1], s[i]
        i+=1
    i+=1
print(*s)