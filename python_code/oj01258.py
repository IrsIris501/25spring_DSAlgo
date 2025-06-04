while True:
    try:
        n = int(input())
    except EOFError:
        break
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))

    min_dist = [100010] + mat[0][1::]
    def find_min(l):
        temp = []
        for i in range(len(l)):
            temp.append((l[i], i))
        return min(temp)
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

