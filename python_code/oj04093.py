def intersection(a: set, b: set) -> set:
    a=list(a)
    out=[]
    for i in a:
        if i in b:
            out.append(i)
    return set(out)

def n_intersection(a: set, b: set) -> set:
    a=list(a)
    out=[]
    for i in a:
        if i not in b:
            out.append(i)
    return set(out)


n=int(input())
inverted_index=[]
for i in range(n):
    temp_list=list(map(int, input().split()))
    inverted_index.append(set(temp_list[1::]))
m=int(input())
for _ in range(m):
    search_list=list(map(int, input().split()))
    for i in range(n):
        if search_list[i]==1:
            break
    start=inverted_index[i]
    for i in range(n):
        if search_list[i]==1:
            start=intersection(start, inverted_index[i])
        elif search_list[i]==-1:
            start=n_intersection(start, inverted_index[i])
    ans=sorted(list(start))
    if ans:
        print(*ans)
    else:
        print("NOT FOUND")







