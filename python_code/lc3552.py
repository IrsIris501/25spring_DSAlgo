from collections import defaultdict, deque


class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        map_map = [[] for i in range(26)]
        for i in range(n):
            for j in range(m):
                if ord('A') <= ord(matrix[i][j]) <= ord('Z'):
                    map_map[ord(matrix[i][j]) - ord('A')].append((i, j))
        q = deque([(0, 0, 0)])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = set()
        visited_gateway = set()
        while q:
            x, y, step = q.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                if x == n-1 and y == m-1:
                    return step
                if ord('A') <= ord(matrix[x][y]) <= ord('Z'):
                    if matrix[x][y] not in visited_gateway:
                        for i in range(n):
                            for j in range(m):
                                if matrix[i][j] == matrix[x][y] and (i, j) != (x, y) and (i, j) not in visited:
                                    q.appendleft((i, j, step))
                        visited_gateway.add(matrix[x][y])



                for i in range(4):
                    if (x + dx[i], y + dy[i]) not in visited and 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and matrix[x + dx[i]][y + dy[i]] != '#':
                        q.append((x + dx[i], y + dy[i], step + 1))
        return -1


