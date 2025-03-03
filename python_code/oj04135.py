import math
def min_cost(n, m, cost):
    left=max(cost)-1
    right=sum(cost)
    while True:
        current=math.ceil((right+left)/2)
        temp=0
        months=1
        for i in cost:
            if temp+i<=current:
                temp+=i
            else:
                temp=i
                months+=1
        if months>m:
            left=current
        elif months<=m:
            right=current

        if right-left==1:
            return right


n, m=map(int, input().split())
cost=[]
for i in range(n):
    cost.append(int(input()))
print(min_cost(n, m, cost))

