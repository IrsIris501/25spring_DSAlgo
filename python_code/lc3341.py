import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = set()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            if x == n-1 and y == m-1:
                return t
            visited.add((x, y))

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < m:
                    heapq.heappush(heap, (max(moveTime[nx][ny] + 1, t + 1), nx, ny))
