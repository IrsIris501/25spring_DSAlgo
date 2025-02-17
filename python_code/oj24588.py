def value(suffix_list):
    stack=[]
    for i in range(len(suffix_list)):
        if suffix_list[i]=='+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif suffix_list[i]=='-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif suffix_list[i]=='*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif suffix_list[i] == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
        else:
            stack.append(float(suffix_list[i]))
    return stack.pop()



n=int(input())
for i in range(n):
    suffix_list=input().split()
    print('%.2f' %value(suffix_list))
