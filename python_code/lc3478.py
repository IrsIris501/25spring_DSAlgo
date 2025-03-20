class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        import heapq
        answer=[0 for i in range(len(nums1))]
        temp=[]
        for i in range(len(nums1)):
            temp.append((nums1[i], nums2[i], i))
        temp.sort(key=lambda x:x[0])
        heap=[]
        s=0
        pointer=0
        for i in range(len(nums1)):
            while pointer<i:
                if temp[pointer][0]<temp[i][0]:
                    heapq.heappush(heap, temp[pointer][1])
                    s+=temp[pointer][1]
                    pointer+=1
                    if len(heap)>k:
                        s-=heapq.heappop(heap)
                else:
                    break
            answer[temp[i][2]]=s
        return answer




