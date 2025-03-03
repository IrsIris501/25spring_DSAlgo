

class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def val(numlist):
            '''
            :param numlist: List[int]
            :return: int
            '''
            out=0
            for i in range(len(numlist)):
                if numlist[i]:
                    out+=2**i
            return out
        if not k:
            return 1
        result=100
        left=0
        right=0
        avail=False
        numlist=[0 for i in range(8)]
        while True:
            if val(numlist)>=k:
                if result>right-left:
                    result=right-left
                temp=list(str(bin(nums[left])))
                temp.reverse()
                i=0
                while temp[i]!='b':
                    numlist[i]-=int(temp[i])
                    i+=1
                left+=1
            else:
                if right!=len(nums):
                    right+=1
                else:
                    break
                temp = list(str(bin(nums[right-1])))
                temp.reverse()
                i = 0
                while temp[i] != 'b':
                    numlist[i] += int(temp[i])
                    i+=1


        if result<100:
            return result
        else:
            return -1

s=Solution()
nums=list(map(int, input().split()))
k=int(input())
print(s.minimumSubarrayLength(nums, k))

