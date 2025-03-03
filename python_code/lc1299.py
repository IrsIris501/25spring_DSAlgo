class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        temp=-1
        arr.reverse()
        dp=[]
        for i in arr:
            dp.append(temp)
            if i>temp:
                temp=i
        dp.reverse()
        return dp

s=Solution()
arr=list(map(int, input().split()))
print(*s.replaceElements(arr))