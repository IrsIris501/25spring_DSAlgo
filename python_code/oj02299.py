# pylint: skip-file

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global ans
    stack = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            stack.append(left[i])
            i += 1
            ans += j
        else:
            stack.append(right[j])
            j += 1
    if i < len(left):
        for k in range(i, len(left)):
            stack.append(left[k])
            ans += j
    elif j < len(right):
        stack += right[j:]
    return stack

while True:
    n = int(input())
    if not n:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    ans = 0
    sorted_arr = merge_sort(arr)
    print(ans)
