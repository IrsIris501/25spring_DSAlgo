n=int(input())
value=list(map(int, input().split()))
dp1=[0 for i in range(n)]
dp2=[0 for i in range(n)]

for i in range(n-1, -1, -1):
    temp=[]
    left=i*2+1
    right=i*2+2
    dp1[i]+=value[i]
    if left<n:
        dp1[i]+=dp2[left]
    if right<n:
        dp1[i]+=dp2[right]
    if left<n:
        dp2[i]+=max(dp2[left], dp1[left])
    if right<n:
        dp2[i]+=max(dp2[right], dp1[right])
print(max(dp1[0], dp2[0]))
