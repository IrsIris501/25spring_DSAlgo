import heapq

t=int(input())
for _ in range(t):
    m, n=map(int, input().split())
    sums=list(map(int, input().split()))
    heapq.heapify(sums)
    for i in range(m-1):
        b=sorted(list(map(int, input().split())))
        heap = []
        visited = set()
        # Push the initial sum of the first elements
        for j in range(n):
            heapq.heappush(heap, (sums[j] + b[0], j, 0))
            visited.add((j, 0))
        sums_temp = []

        while heap and len(sums_temp) < n:
            sum_val, i_sum, i_b = heapq.heappop(heap)
            sums_temp.append(sum_val)
            # Move right in b
            if i_b + 1 < len(b):
                if (i_sum, i_b + 1) not in visited:
                    new_sum = sums[i_sum] + b[i_b + 1]
                    heapq.heappush(heap, (new_sum, i_sum, i_b + 1))
                    visited.add((i_sum, i_b + 1))

                    # Update sums for next iteration
        heapq.heapify(sums_temp)
        sums = sums_temp
    sums.sort()
    print(*sums)