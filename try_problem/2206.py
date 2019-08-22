from collections import deque
from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]
matrix = []
visited = [[False for j in range(m)] for i in range(n)]
distance = [[0 for j in range(m)] for i in range(n)]
max_distance = []

for i in range(n):
    component = [int(x) for x in stdin.readline().strip()]
    matrix.append(component)


def bfs(convert_matrix, new_visited, new_distance):
    q = deque()
    q.append([0, 0])
    new_visited[0][0] = True
    new_distance[0][0] = 1

    while q:
        y, x = q.popleft()
        vectors = [[y-1, x], [y, x-1], [y+1, x], [y, x+1]]
        for next_y, next_x in vectors:
            if next_y < 0 or next_x < 0 or next_y >= n or next_x >= m:
                continue

            if new_visited[next_y][next_x] or convert_matrix[next_y][next_x] == 1:
                continue

            q.append([next_y, next_x])
            new_distance[next_y][next_x] = new_distance[y][x] + 1
            new_visited[next_y][next_x] = True

    if n == 1 and m == 1:
        max_distance.append(1)
    elif new_visited[n-1][m-1]:
        max_distance_value = max(map(max, new_distance))
        max_distance.append(max_distance_value)
    else:
        max_distance.append(-1)


convert_vector_list = [[0, 0]]
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1:
            convert_vector_list.append([j, i])


for j, i in convert_vector_list:
    matrix[j][i] = 0
    bfs(matrix, visited, distance)
    if j == 0 and i == 0:
        continue
    matrix[j][i] = 1

answer_value = max(max_distance)
print(answer_value)

# if answer_value == 0:
#     print(-1)
# else:
#     print(answer_value)
