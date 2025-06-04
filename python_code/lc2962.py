class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0
        right = 0
        ans = 0
        m = max(nums)
        for i in range(n):

            if i > 0 and nums[i-1] == m:
                count -= 1
            while right < n and count < k:
                if nums[right] == m:
                    count += 1
                right += 1
            if count == k:
                ans += n - right + 1
            elif right == n:
                break
        return ans
