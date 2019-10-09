"""
우선 주어진 정보를 정리를 할 필요가 있다.
- 인접 행렬을 인접 리스트로 정리한다. 이렇게 하면 속도적인 측면에서 더 낫다.
- 코드상에서 adjacency_list가 인접 리스트이다.

그 뒤로 문제의 요구사항에 맞게 변경하기 위한 과정이다.
bfs를 이용하였다.

1. 0~n-1까지로 표현되는 방문 확인용 리스트 생성
2. 방문 한 곳을 담을 수 있는 방문 리스트 생성
3. result_edges에서 해당하는 경우에 한해 숫자를 1로 변경해주는 코드 작성
4. bfs run
5. 마지막 정답 출력을 파이썬의 언팩킹 기능을 이용해서 깔끔하게 정리하였다.
"""


from collections import deque
from sys import stdin

n = int(input())

edges = []
for i in range(n):
    edge = [int(x) for x in stdin.readline().split()]
    edges.append(edge)


# Matrix to List

adjacency_list = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if edges[i][j] == 0:
            continue

        adjacency_list[i].append(j)


result_edges = [[0 for i in range(n)] for i in range(n)]


def bfs(start_v):
    q = deque()
    for end_v in adjacency_list[start_v]:
        q.append(end_v)

    visited = ["white" for i in range(n)]
    visited_vertex_number_list = []

    while q:
        u = q.popleft()

        if visited[u] == 'white':
            visited_vertex_number_list.append(u)
            visited[u] = 'gray'

            for vertex_number in adjacency_list[u]:
                q.append(vertex_number)

    for i in range(n):
        if start_v != i:
            continue

        for visited_vertex_number in visited_vertex_number_list:
            result_edges[start_v][visited_vertex_number] = 1


for i in range(n):
    bfs(i)

for result_edge in result_edges:
    print(*result_edge)