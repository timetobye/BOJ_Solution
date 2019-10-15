"""
각 점에서 bfs를 시행한 다음 거리의 총합을 비교하면 되는 문제
근데 왜 안 풀려......--

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

