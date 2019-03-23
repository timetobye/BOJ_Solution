"""
1. A가 B를 신뢰하는 경우에는 B - > A
2. 간선 정보를 받고 bfs를 만든다.(dfs로 하니까 시간 초과 났음)
3. 출발 정점에 따라 가장 멀리 갈 수 있는 것이 무엇인지 확인해 보자 그러기 위해서는 방문 지점 초기화를 해야 할 듯

python3 제출하면 시간 초과가 나므로 PyPy3으로 제출하였음
"""
from sys import stdin
from collections import deque

n, m = [int(x) for x in stdin.readline().split()]

edges = []
for i in range(m):
    edge = [int(x) for x in stdin.readline().split()]
    edges.append(edge)

r = [[] for i in range(n + 1)]
check = []

for u, v in edges:
    r[v].append(u)

comp = [0]


def bfs(u):
    q = deque()
    q.append(u)
    color[u] = "gray"
    global value

    while q:
        u = q.popleft()
        for v in r[u]:
            if color[v] == "white":
                color[v] = "gray"
                q.append(v)
                value += 1


for i in range(1, n + 1):
    color = ["white" for j in range(n + 1)]
    value = 0
    if color[i] == "white":
        bfs(i)
    comp.append(value)

max_value = max(comp)

for i in range(n+1):
    if max_value == comp[i]:
        print(i, end=" ")
