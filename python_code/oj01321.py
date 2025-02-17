# pylint: skip-file
def chess(chessboard, n, k, start):
    global count
    if k==0:
        count+=1
        return
    for i in range(start, n):
        for j in range(n):
            if chessboard[i][j]=='#' and not visited[i][j]:
                for l in range(n):
                    visited[i][l]+=1
                    visited[l][j]+=1
                chess(chessboard, n, k-1, i+1)
                for l in range(n):
                    visited[i][l]-=1
                    visited[l][j]-=1

    return

while True:
    n, k=map(int, input().split())
    visited=[[0 for i in range(n)] for j in range(n)]
    if (n, k)==(-1, -1):
        break
    chessboard=[]
    for i in range(n):
        temp=list(input())
        chessboard.append(temp)
    image=chessboard
    count=0
    chess(chessboard, n, k, 0)
    print(count)