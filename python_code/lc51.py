class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        global solutions
        def is_safe(col, board):
            for i in range(len(board)):
                if board[i]==col:
                    return False
                if abs(col-board[i])==abs(len(board)-i):
                    return False
            return True

        solutions=[]

        def backtrack(board, n):
            global solutions
            if len(board)==n:
                temp=[]
                for i in range(n):
                    temp.append('.'*board[i]+'Q'+'.'*(n-board[i]-1))
                solutions.append(temp)
                return
            for i in range(n):
                if is_safe(i, board):
                    backtrack(board+[i], n)

        backtrack([], n)
        return solutions

s=Solution()
n=int(input())
print(*s.solveNQueens(n))



