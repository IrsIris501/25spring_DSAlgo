class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        right = 0
        cnt = dict()
        n = len(nums)
        ans = 0
        distinct = len(set(nums))
        for i in range(n):
            if i != 0:
                cnt[nums[i - 1]] -= 1
                if cnt[nums[i - 1]] == 0:
                    cnt.pop(nums[i - 1])
            while right < n and len(cnt) < distinct:
                cnt[nums[right]] = cnt.get(nums[right], 0) + 1
                right += 1
            if len(cnt) == distinct:
                ans += n - right + 1
        return ans



