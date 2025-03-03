class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=int(100000)
        max_profit=0
        for i in range(len(prices)):
            if prices[i]-min_price>max_profit:
                max_profit=prices[i]-min_price
            if prices[i]<min_price:
                min_price=prices[i]
        return max_profit

s=Solution()
prices=list(map(int, input().split()))
print(s.maxProfit(prices))

