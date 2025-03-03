def min_int(n, k):
    '''

    :param n: list[str]
    :param k: int
    :return: int
    '''
    stack=[]
    for i in n:
        while k and stack and stack[-1]>i:
            stack.pop()
            k-=1
        stack.append(i)
    while k:
        stack.pop()
        k-=1
    out=''
    for i in stack:
        out+=i
    return int(out)

t=int(input())
for i in range(t):
    n, k=input().split()
    n=list(n)
    k=int(k)
    print(min_int(n, k))


