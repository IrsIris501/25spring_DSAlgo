from collections import defaultdict, deque
from copy import deepcopy


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(set)
        self.reverse_graph = defaultdict(set)
        self.num = n
    def add_edge(self, x, y):
        self.graph[x].add(y)
        self.reverse_graph[y].add(x)

def find_inconsistency(graph: Graph):
    q = deque()
    count = 0
    for i in range(graph.num):
        if graph.reverse_graph[i] == set():
            q.append(i)
    while q:
        cur = q.popleft()
        count += 1
        for i in graph.graph[cur]:
            graph.reverse_graph[i].remove(cur)
            if graph.reverse_graph[i] == set():
                q.append(i)
    return count != graph.num

def topological_sort(graph: Graph):
    q = deque()
    seq = []
    for i in range(graph.num):
        if graph.reverse_graph[i] == set() and graph.graph[i] != set():
            q.append((i, 0))
            break
    while q:
        cur, layer = q.popleft()
        seq.append(cur)
        for i in list(graph.graph[cur]):
            graph.reverse_graph[i].remove(cur)
            if graph.reverse_graph[i] == set():
                q.append((i, layer + 1))
    if layer == n-1:
        return seq
    else:
        return []

def solve(stack, n, m):
    graph = Graph(n)
    for i in range(m):
        i1, i2 = stack[i]
        graph.add_edge(i1, i2)
        temp = deepcopy(graph)
        if find_inconsistency(temp):
            print(f'Inconsistency found after {i+1} relations.')
            return
        temp = deepcopy(graph)
        ans = topological_sort(temp)
        if len(ans) == n:
            ans_str = ''
            for j in ans:
                ans_str += chr(j + ord('A'))
            print(f'Sorted sequence determined after {i+1} relations: {ans_str}.')
            return
    print('Sorted sequence cannot be determined.')
    return

while True:
    n, m = map(int, input().split())
    if not n:
        break
    stack = []
    for i in range(m):
        s = input()
        index1 = ord(s[0]) - ord('A')
        index2 = ord(s[-1]) - ord('A')
        stack.append((index1, index2))
    solve(stack, n, m)


