from collections import deque


class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        suffix = deque()
        temp = 0
        for i in range(n):
            temp |= nums[i]
            prefix.append(temp)
        temp = 0
        for i in range(n-1, -1, -1):
            temp |= nums[i]
            suffix.appendleft(temp)
        suffix.append(0)
        ans = 0
        for i in range(n):
            ans = max(ans, prefix[i] | (nums[i] << k) | suffix[i+1])
        return ans

