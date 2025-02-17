n, m=map(int, input().split())
nums=list(map(int, input().split()))
def C(nums, i):
    for j in range(len(nums)):
        nums[j]=(nums[j]+i)%65536
    return
def Q(nums, i):
    tmp=0
    for j in nums:
        a=str(bin(j))
        if j>=2**(i) and a[-i-1]!='0':
            tmp+=1
    return tmp
for _ in range(m):
    s=input()
    if s[0]=='Q':
        print(Q(nums, int(s[2::])))
    else:
        C(nums, int(s[2::]))

