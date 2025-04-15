class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)
        palindrome=[[False for j in range(n)] for i in range(n)]
        global ans
        ans=[]

        for i in range(n):
            palindrome[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                palindrome[i][i+1]=True
        for j in range(n):
            for i in range(j-1):
                if s[i]==s[j]:
                    palindrome[i][j]=palindrome[i+1][j-1]
        def dfs(i, route: list[str]):
            global ans
            if i==n:
                ans.append(route)
                return
            for j in range(i+1, n+1):
                if palindrome[i][j-1]:
                    dfs(j, route+[s[i:j]])

        dfs(0, [])
        return ans

sol=Solution()
s=input()
print(sol.partition(s))


