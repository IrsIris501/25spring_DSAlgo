class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        vis=set()
        def backtrack(first: int, output: list[int]):
            if first==n:
                ans.append(output)
                return
            for i in range(n):
                if nums[i] not in vis:
                    vis.add(nums[i])
                    backtrack(first+1, output+[nums[i]])
                    vis.remove(nums[i])
        backtrack(0, [])

        return ans


s=Solution()
print(s.permute([i for i in range(1, 4)]))