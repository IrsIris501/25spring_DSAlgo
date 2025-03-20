class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0]<=intervals[i-1][1]:
                intervals[i][0]=intervals[i-1][0]
                intervals[i][1]=max(intervals[i][1], intervals[i-1][1])
                intervals[i-1]=0
        ans=[]
        for i in intervals:
            if i!=0:
                ans.append(i)
        return ans

n=int(input())
intervals=[]
for i in range(n):
    a, b=map(int, input().split())
    intervals.append([a, b])
s=Solution()
print(s.merge(intervals))





