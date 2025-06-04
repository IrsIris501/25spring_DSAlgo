class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        global ans
        if not digits:
            return []
        map_dict=dict()
        for i in range(2, 7):
            map_dict[i]=[chr(ord('a')+3*(i-2)), chr(ord('a')+3*(i-2)+1), chr(ord('a')+3*(i-2)+2)]
        map_dict[7]=['p', 'q', 'r', 's']
        map_dict[8]=['t', 'u', 'v']
        map_dict[9]=['w', 'x', 'y', 'z']

        ans=[]
        def dfs(digits: str, cur=''):
            global ans
            temp=digits[0]
            if len(digits)==1:
                for i in map_dict[int(temp)]:
                    ans.append(cur+i)
                return
            else:
                for i in map_dict[int(temp)]:
                    dfs(digits[1::], cur+i)


        dfs(digits)
        return ans
s=Solution()
digits=input()
print(s.letterCombinations(digits))


