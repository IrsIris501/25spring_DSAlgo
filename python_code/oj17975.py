
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
def insert_element(hash_table, ele: int, m):
    pos = ele % m
    if not hash_table[pos] or hash_table[pos] == ele:
        hash_table[pos] = ele
        return pos
    else:
        k = 1
        while True:
            npos = (pos + k * k) % m
            if not hash_table[npos] or hash_table[npos] == ele:
                hash_table[npos] = ele
                return npos
            npos = (pos - k * k) % m
            if not hash_table[npos] or hash_table[npos] == ele:
                hash_table[npos] = ele
                return npos
            k += 1





l = [None for i in range(m)]
ans = []
for i in num_list:
    temp = insert_element(l, i, m)
    ans.append(temp)
print(*ans)
