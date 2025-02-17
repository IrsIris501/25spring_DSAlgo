import bisect
nums=list(map(int, input().split()))
target=int(input())
print(bisect.bisect_left(nums, target))