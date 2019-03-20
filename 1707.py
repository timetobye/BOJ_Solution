import sys
from sys import stdin
sys.setrecursionlimit(10000000)

tc = int(stdin.readline())

for _ in range(tc):
    info = [int(x) for x in stdin.readline().split()]
    n, k = info[0], info[1]

    edges = []
    for i in range(k):
        temp = [int(x) for x in stdin.readline().split()]
        edges.append(temp)

    # make adjacency list
    r = [[] for i in range(n + 1)]

    for u, v in edges:
        r[u].append(v)
        r[v].append(u)

    color = ["white" for i in range(n + 1)]
    dist = [None for i in range(n + 1)]


    def dfs(u):
        color[u] = "black"
        for v in r[u]:
            if color[v] == "white":
                color[v] = "black"
                dist[v] = dist[u] + 1
                dfs(v)


    for start_v in range(1, n + 1):
        if dist[start_v] is None:
            dist[start_v] = 1
            dfs(start_v)


    def check_bi(u):
        for v in r[u]:
            if (dist[u] % 2) == (dist[v] % 2):
                return False

        return True


    for i in range(1, n + 1):
        if not check_bi(i):
            print("NO")
            break
    else:
        print("YES")
