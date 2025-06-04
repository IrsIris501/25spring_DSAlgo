from heapq import *
from collections import defaultdict

p=int(input())
graph=dict()
places=[]

for i in range(p):
    temp=input()
    places.append(temp)
    graph[temp]=[]


q=int(input())
for i in range(q):
    ini, fin, l=input().split()
    l=int(l)
    graph[ini].append((l, fin))
    graph[fin].append((l, ini))


r=int(input())
for _ in range(r):
    path=defaultdict(list)
    dist_dict=dict()
    shortest=defaultdict(bool)

    start, end=input().split()
    if start==end:
        print(start)
        break
    heap=[]
    heappush(heap, (0, start))
    while heap:
        dist, pos=heappop(heap)
        if pos==end:
            path_ans=''
            for i in path[pos]:
                path_ans+=i[0]
                path_ans+='->('
                path_ans+=str(i[1])
                path_ans+=')->'
            path_ans+=end
            print(path_ans)
            break
        shortest[pos]=True
        for i in graph[pos]:
            length=i[0]
            npos=i[1]
            if dist+length<dist_dict.get(npos, 100000):
                dist_dict[npos]=dist+length
                heappush(heap, (dist+length, npos))
                path[npos]=path[pos]+[(pos, length)]

