class Solution:
    def longestPalindrome(self, s: str) -> str:
        lists=[]
        for i in range(len(s)):
            lists.append('#')
            lists.append(s[i])
        lists.append('#')
        ans=''
        max_len=0
        max_palindrome=[]
        for i in range(len(lists)):
            left=i
            right=i
            while left!=0 and right!=len(lists)-1:
                left-=1
                right+=1
                if lists[left]!=lists[right]:
                    if (right-left-2)/2>=max_len:
                        max_len=(right-left-2)//2
                        max_palindrome=lists[left+1:right]
                    break
                elif left==0 or right==len(lists)-1:
                    if (right-left)/2>=max_len:
                        max_len=(right-left)//2
                        max_palindrome=lists[left+1:right]

                    break
        for i in max_palindrome:
            if i!='#':
                ans+=i
        return ans

s=Solution()
print(s.longestPalindrome(input()))







