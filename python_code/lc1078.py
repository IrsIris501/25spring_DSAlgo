class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        text_list=text.split()
        ans=[]
        for i in range(len(text_list)):
            if i!=0 and i!=len(text_list)-1:
                if text_list[i-1]==first and text_list[i]==second:
                    ans.append(text_list[i+1])
        return ans

text=input()
first=input()
second=input()
s=Solution()
print(*s.findOcurrences(text, first, second))