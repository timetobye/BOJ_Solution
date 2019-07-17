import sys
from sys import stdin
from collections import deque
sys.setrecursionlimit(10000000)

test_case = int(input())

for _ in range(test_case):
    n, k = [int(x) for x in stdin.readline().split()]
    time = [int(x) for x in stdin.readline().split()]
    time.insert(0, 0)
    dp = [0 for i in range(n + 1)]

    in_degree = [0 for i in range(n + 1)]
    edges = []
    for i in range(k):
        temp = [int(x) for x in stdin.readline().split()]
        edges.append(temp)

    building_number = int(input())

    r = [[] for i in range(n+1)]

    for u, v in edges:
        r[u].append(v)
        in_degree[v] += 1

    topologically_sorted_vertices = []
    checked = [False for i in range(n + 1)]


    def topology(u):
        q = deque()
        q.append(u)
        dp[u] = time[u]
        while q:
            u = q.popleft()
            if in_degree[u] == 0:
                topologically_sorted_vertices.append(u)
                checked[u] = True
                for v in r[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        q.append(v)
                    dp[v] = max(dp[v], dp[u] + time[v])


    for i in range(1, n + 1):
        if not checked[i]:
            topology(i)

    print(dp[building_number])
