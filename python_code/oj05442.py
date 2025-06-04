from collections import defaultdict
n = int(input())
mat = [[100010 for i in range(n)] for j in range(n)]
for i in range(n-1):
    temp = input().split()
    pos = ord(temp[0]) - ord('A')
    mat[pos][pos] = 0
    m = int(temp[1])
    index = 2
    for j in range(m):
        pos2 = ord(temp[index]) - ord('A')
        index += 1
        length = int(temp[index])
        mat[pos][pos2] = length
        mat[pos2][pos] = length
        index += 1

def find_min(l):
    min_l, min_i = float('inf'), 0
    for i in range(len(l)):
        if l[i] < min_l:
            min_l = l[i]
            min_i = i
    return min_l, min_i
min_dist = [100010] + mat[0][1::]
white = set()
white.add(0)
ans = 0
for _ in range(n-1):
    dist, pos = find_min(min_dist)
    ans += dist
    white.add(pos)
    min_dist[pos] = 100010
    for i in range(n):
        if i not in white:
            min_dist[i] = min(min_dist[i], mat[i][pos])

print(ans)




