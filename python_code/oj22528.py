score=[float(x) for x in input().split()]
n=len(score)

def adjust(a, x):
    return a*x+1.1**(a*x)
left=0
right=1000000000
while right-left!=1:
    mid=(left+right)//2
    count=0
    for i in score:
        if adjust(mid/1000000000, i)>=85:
            count+=1
    if count>=0.6*n:
        right=mid
    else:
        left=mid
print(right)