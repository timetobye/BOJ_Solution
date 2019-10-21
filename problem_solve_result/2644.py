from collections import deque
from sys import stdin

n = int(stdin.readline())
cousin_one, cousin_two = [int(x) for x in stdin.readline().split()]
m = int(stdin.readline())

edges = []

for i in range(m):
    edge = [int(x) for x in stdin.readline().split()]
    edges.append(edge)


r = [[] for i in range(n + 1)]

for u, v in edges:
    r[u].append(v)
    r[v].append(u)

distance = [0 for i in range(n + 1)]
visited = ["white" for i in range(n + 1)]


def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited[start_v] = 'gray'

    while q:
        u = q.popleft()
        for v in r[u]:
            if visited[v] == 'white':
                visited[v] = 'gray'
                distance[v] = distance[u] + 1
                q.append(v)


bfs(cousin_one)
cousin_relation_result = distance[cousin_two]

if cousin_relation_result == 0:
    print(-1)
else:
    print(cousin_relation_result)
