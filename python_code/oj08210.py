import math

l, n, m=map(int, input().split())
stones=[0]
for i in range(n):
    stones.append(int(input()))
stones.append(l)
left=1
right=l
while True:
    current=int(math.ceil((left+right)/2))
    count=0
    temp=0
    for i in range(1, len(stones)):
        if stones[i]-temp<current:
            count+=1
        else:
            temp=stones[i]
    if count>m:
        right=current-1
    elif count<=m:
        left=current
    if left==right:
        print(right)
        break


