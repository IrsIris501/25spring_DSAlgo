class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        import math
        right=max(nums)
        left=0
        while True:
            current=int(math.ceil((right+left)/2))
            operations=0
            for i in nums:
                operations+=math.ceil(i/current)-1
            if operations>maxOperations:
                left=current
            elif operations<=maxOperations:
                right=current
            if right-left==1:
                return right
            if current==1:
                return 1

nums=list(map(int, input().split()))
maxOperations=int(input())
s=Solution()
print(s.minimumSize(nums, maxOperations))




