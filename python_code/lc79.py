class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        global avail
        avail=False
        def dfs(x, y, i: int):
            global avail

            if i==l:
                avail=True
                return
            for j in range(4):
                nx=x+dx[j]
                ny=y+dy[j]
                if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and board[nx][ny]==word[i]:
                    visited.add((nx, ny))
                    dfs(nx, ny, i+1)
                    visited.remove((nx, ny))

        dx=[1, -1, 0, 0]
        dy=[0, 0, 1, -1]
        n=len(board)
        m=len(board[0])
        l=len(word)
        for j in range(n):
            for k in range(m):
                if board[j][k]==word[0]:
                    visited=set()
                    visited.add((j, k))
                    dfs(j, k, 1)
                    if avail:
                        return True
        return False

s=Solution()
word=input()
n=int(input())
board=[]
for i in range(n):
    board.append(input().split())
print(s.exist(board, word))



