class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp=nums[0]
        for i in range(1, len(nums)):
            temp^=nums[i]
        return temp

nums=list(map(int, input().split()))
s=Solution()
print(s.singleNumber(nums))
