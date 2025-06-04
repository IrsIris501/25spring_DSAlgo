class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        flight_map=[[-1 for i in range(n)] for j in range(n)]
        f = [[-1 for i in range(n)] for j in range(k+1)]
        for fro, to, price in flights:
            flight_map[fro][to]=price
            if fro==src:
                f[0][to]=price
        for i in range(1, k+1):
            for j in range(n):
                min_price=10000000
                for l in range(n):
                    if flight_map[l][j]!=-1 and f[i-1][l]!=-1 and f[i-1][l]+flight_map[l][j]<min_price:
                        min_price=f[i-1][l]+flight_map[l][j]
                if min_price<10000000:
                    f[i][j]=min_price
        ans=10000000
        for i in range(k+1):
            if f[i][dst]!=-1 and f[i][dst]<ans:
                ans=f[i][dst]
        if ans<10000000:
            return ans
        else:
            return -1

