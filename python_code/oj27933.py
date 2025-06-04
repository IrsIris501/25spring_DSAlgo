n = int(input())
stack = []
nex = 1
count = 0
for i in range(2*n):
    s = input()
    if s[0] == 'a':
        s = s.split()
        stack.append(int(s[1]))
    else:
        if stack[-1] == nex:
            stack.pop()
        else:
            stack.sort(reverse = True)
            count += 1
            stack.pop()
        nex += 1
print(count)

