import sys
sys.setrecursionlimit(10**6)

def get_cycle(n, arr):
    edges = []

    for i in range(1, n + 1):
        info = [i, arr[i]]
        edges.append(info)

    # make adjacency list
    r = [[] for i in range(n + 1)]

    for u, v in edges:
        r[u].append(v)

    color = ["white" for i in range(n + 1)]
    dist = [None for i in range(n + 1)]

    def dfs(u, value):
        for v in r[u]:
            if color[v] == "white":
                color[v] = "gray"
                dist[v] = value
                dfs(v, value)

        color[u] = "black"

    for i in range(1, n + 1):
        dfs(i, i)

    print(len(set(dist))-1)


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())  # number of vertex
        arr = [int(x) for x in input().split()]
        arr.insert(0, 0)
        get_cycle(n, arr)