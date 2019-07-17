from collections import deque

n = int(input())  # number of vertex
m = int(input())  # number of edges

# 양방향 그래프 만들기
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])
    edges.append([b, a])

# make Adjancecy List
r = [[] for j in range(n + 1)]
for u, v in edges:
    r[u].append(v)

# bfs
INF = 99999
dist = [INF for j in range(n + 1)]
parent = [None for j in range(n + 1)]
color = ["white" for j in range(n + 1)]

# start_vertex
start_v = 1

dist[start_v] = 0
parent[start_v] = None
color[start_v] = "gray"

que = deque()
que.append(start_v)

while que:
    u = que.popleft()
    for v in r[u]:
        if color[v] == "white":
            color[v] = "gray"
            parent[v] = u
            dist[v] = dist[u] + 1
            que.append(v)
    color[u] = "black"

count = 0
for i in dist:
    if i == 1 or i == 2:
        count += 1

print(count)