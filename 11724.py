import sys
from sys import stdin
sys.setrecursionlimit(10000000)

n, k = [int(x) for x in stdin.readline().split()]

edges = []

for i in range(k):
    edge = [int(x) for x in stdin.readline().split()]
    edges.append(edge)

r = [[] for i in range(n + 1)]


for u, v in edges:
    r[u].append(v)
    r[v].append(u)

dist = [0 for i in range(n + 1)]
start = [0 for i in range(n + 1)]
end = [0 for i in range(n + 1)]
color = ["white" for i in range(n + 1)]
timestamp = 0


def dfs(u, value):
    global timestamp

    timestamp += 1
    start[u] = (timestamp, value)
    for v in r[u]:
        if color[v] == "white":
            color[v] = "gray"
            dist[v] = dist[u] + 1
            dfs(v, value)

    timestamp += 1
    end[u] = (timestamp, value)
    color[u] = "black"


count = 0
for i in range(1, n + 1):
    if color[i] == "white":
        dfs(i, count)
        count += 1

print(count)

# for i, start_end in enumerate(zip(start, end)):
#     print(f'{i} : {start_end}')

