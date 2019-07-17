import sys
from sys import stdin
from pprint import pprint
sys.setrecursionlimit(10000000)

n = int(input())  # number of vertex

adjacency_matrix = []
for i in range(n):
    row = [int(x) for x in stdin.readline().split()]
    adjacency_matrix.append(row)


# convert adjacency_matrix to adjacency list
r = [[] for i in range(n + 1)]
color = [[] for i in range(n + 1)]

in_degree = [0 for i in range(1 + n)]
out_degree = [0 for i in range(1 + n)]

for i in range(n):
    for j in range(n):
        if adjacency_matrix[i][j] == 1:
            r[i + 1].append(j + 1)
            in_degree[j + 1] += 1
            out_degree[i + 1] += 1

for i in range(1, n + 1):
    if (in_degree[i] % 2) != 0 or (in_degree[i] != out_degree[i]):
        euler_check = False
        break
else:
    euler_check = True

color = [["white" for j in range(n + 1)] for i in range(n + 1)]
visited = ["non_visited" for i in range(n + 1)]
euler_point = []

component = 0


def dfs(u):
    visited[u] = "visited"
    global component

    for v in r[u]:
        if color[u][v] == "white":
            color[u][v] = "gray"
            color[v][u] = "gray"
            dfs(v)


# component check
for i in range(1, n + 1):
    if visited[i] == "non_visited":
        dfs(i)
        component += 1


color = [["white" for j in range(n + 1)] for i in range(n + 1)]
visited = ["non_visited" for i in range(n + 1)]


def new_dfs(u):
    visited[u] = "visited"

    for v in r[u]:
        if color[u][v] == "white":
            color[u][v] = "gray"
            color[v][u] = "gray"
            new_dfs(v)

    euler_point.append(u)


if component > 1:
    print(-1)
elif euler_check:
    for i in range(1, n + 1):
        if visited[i] == "non_visited":
            new_dfs(i)
    euler_point.reverse()
    print(*euler_point)
else:
    print(-1)