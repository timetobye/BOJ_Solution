"""
1. 주어진 조건은 양방향 그래프를 구성하는 조건
2. 인접 리스트를 이용해서 구현
3. bfs를 이용
4. 시작 위치부터 white에서 gray로 색칠하면서 이동 할 수 있는 곳들을 gray로 변경
5. 4와 동시에 이동 거리도 1씩 늘림
6. 각 시작 지점별 이동 거리의 총합을 구해서 나열
7. 이동 거리 최소 값을 찾고 그 중 index 번호를 구함
8. python의 index는 찾는 값 중 가장 먼저 있는 값이 index 번호를 리턴합니다.
9. 주어진 조건은 1부터 시작하니까 index 번호 + 1이 답
"""


from collections import deque
from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]

adjacency_list = [[] for _ in range(n + 1)]

for i in range(m):
    friend_number_one, friend_number_two = [int(x) for x in stdin.readline().split()]
    adjacency_list[friend_number_one].append(friend_number_two)
    adjacency_list[friend_number_two].append(friend_number_one)


for i, value in enumerate(adjacency_list):
    adjacency_list[i] = list(set(adjacency_list[i]))


def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited = ["white" for i in range(n+1)]
    distance_list = [0 for i in range(n+1)]
    visited[start_v] = 'gray'

    while q:
        u = q.popleft()

        for v in adjacency_list[u]:
            if visited[v] == "white":
                visited[v] = 'gray'
                q.append(v)
                distance_list[v] = distance_list[u] + 1

    return sum(distance_list)


sum_distance_result = []

for i in range(1, n+1):
    value = bfs(i)
    sum_distance_result.append(value)


print(sum_distance_result.index(min(sum_distance_result)) + 1)

