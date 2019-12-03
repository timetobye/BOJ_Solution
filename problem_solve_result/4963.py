from collections import deque
from sys import stdin

while True:
    width, height = [int(x) for x in stdin.readline().split()]

    if width == 0 and height == 0:
        break

    island_matrix = []
    island_vector = []

    for i in range(height):
        map_info = [int(x) for x in stdin.readline().split()]
        island_matrix.append(map_info)

        for j in range(width):
            if map_info[j] == 1:
                island_vector.append([i, j])

    visited = [["white" for j in range(width)] for i in range(height)]
    distance = [[0 for j in range(width)] for i in range(height)]


    def bfs(y, x, distance_value):
        q = deque()
        q.append([y, x])
        visited[y][x] = 'gray'
        distance[y][x] = distance_value

        while q:
            y,x = q.popleft()
            adjacent_vector = [
                [y-1, x], [y+1, x],
                [y, x-1], [y, x+1],
                [y-1, x-1], [y+1, x-1],
                [y-1, x+1], [y+1, x+1]
            ]

            for next_y, next_x in adjacent_vector:
                if next_y < 0 or next_y >= height or next_x < 0 or next_x >= width:
                    continue

                if visited[next_y][next_x] == 'gray' or island_matrix[next_y][next_x] == 0:
                    continue

                q.append([next_y, next_x])
                distance[next_y][next_x] = distance_value
                visited[next_y][next_x] = 'gray'


    if len(island_vector) == 0:
        print(0)
    else:
        distance_value = 0
        for i, vector in enumerate(island_vector):
            y_vector = vector[0]
            x_vector = vector[1]
            if visited[y_vector][x_vector] == 'white':
                distance_value += 1
            else:
                continue

            bfs(y_vector, x_vector, distance_value)
        print(distance_value)




