count = 0
while True:
    n = int(input())
    if not n:
        break
    s = input()
    count += 1
    length = 0
    lps = [0 for i in range(n)]
    for i in range(1, n):
        while length > 0 and s[i] != s[length]:
            length = lps[length-1]
        if s[i] == s[length]:
            length += 1
            lps[i] = length
    print(f'Test case #{count}')
    for i in range(1, n):
        if (i + 1) // (i + 1 - lps[i]) >= 2 and (i + 1) % (i + 1 - lps[i]) == 0 and lps[i] > 0:
            print(i + 1, (i + 1) // (i + 1 - lps[i]))
    print()
