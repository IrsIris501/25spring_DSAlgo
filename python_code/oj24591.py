def suffixize(s):
    '''
    param s: string
    return: list
    '''
    symbols=['+', '-', '*', '/']
    prime={'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')':0}
    number=[]
    action=[]
    temp=''
    s=list(s)
    while s[-1]==' ':
        s.pop()
    s+=['end']
    for i in range(len(s)):
        if s[i] in symbols:
            if temp!='':
                number.append(temp)
                temp=''
            if action:
                while prime[action[-1]]>=prime[s[i]]:
                    number.append(action.pop())
                    if not action:
                        break
            action.append(s[i])
        elif s[i]=='(':
            if temp!='':
                number.append(temp)
                temp=''
            action.append(s[i])
        elif s[i]==')':
            if temp!='':
                number.append(temp)
                temp=''
            while action[-1]!='(':
                number.append(action.pop())
                if not action:
                    break
            action.pop()
        elif s[i]!='end':
            temp+=s[i]
        else:
            if temp!='':
                number.append(temp)
                temp=''
    while action:
        number.append(action.pop())
    return number

n=int(input())
for _ in range(n):
    s=input()
    print(*suffixize(s))





