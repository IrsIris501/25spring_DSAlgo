from collections import deque


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]
        q=deque()
        q.append([nums[0]])
        q.append([])
        cur=1
        count=0
        while q:
            temp=q.popleft()
            count+=1
            if cur!=len(nums):
                q.append(temp+[nums[cur]])
                q.append(temp)
                if count==2**cur:
                    cur+=1
                    count=0
            else:
                q.append(temp)
                break
        return list(q)

s=Solution()
nums=list(map(int, input().split()))
print(s.subsets(nums))

