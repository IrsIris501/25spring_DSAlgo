class Solution:
    def maxArea(self, height: list[int]) -> int:
        vol=[]
        left=0
        right=len(height)-1
        while True:
            vol.append((right-left)*min(height[left], height[right]))
            if height[left]<height[right]:
                i=left+1
                while True:
                    if height[i]<=height[left] and i<right:
                        i+=1
                    elif i==right:
                        return max(vol)
                    elif height[i]>height[left]:
                        left=i
                        break
            else:
                i=right-1
                while True:
                    if height[i]<=height[right] and i>left:
                        i-=1
                    elif i==left:
                        return max(vol)
                    elif height[i]>height[right]:
                        right=i
                        break

s=Solution()
height=list(map(int, input().split()))
print(s.maxArea(height))


