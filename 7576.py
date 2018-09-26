from collections import deque  # 큐

n, m = map(int, input().split())

data = []
for x in range(m):  # 토마토 밭을 만들자
    data.append(input().split())

start = []
for j in range(len(data)):
    for k in range(len(data[j])):  # 시작 위치를 찾아 보자
        if data[j][k] == '1':
            start.append([j, k])

block = []
for j in range(len(data)):
    for k in range(len(data[j])):  # 블록 위치를 찾아 보자
        if data[j][k] == '-1':
            block.append([j, k])

distance = [[0 for j in range(n)] for i in range(m)]
visited = [[False for j in range(n)] for i in range(m)]
ct = 0
for cnt in data:
    ct += cnt.count('0')
    ct += cnt.count('1')


def bfs(start):
    q = deque()
    for temp in start:
        q.append(temp)  # 큐는 반복을 돌릴 수 없다.
    for y, x in start:
        distance[y][x] = 1
        visited[y][x] = True
    while q:
        y, x = q.popleft()
        adjacents = [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]
        for next_y, next_x in adjacents:
            if next_y < 0 or next_y >= m or next_x < 0 or next_x >= n:
                continue
            if not visited[y][x] or data[next_y][next_x] == '1' or distance[next_y][next_x] != 0 or data[next_y][
                next_x] == '-1':
                continue
            q.append((next_y, next_x))
            visited[next_y][next_x] = True
            distance[next_y][next_x] = distance[y][x] + 1


bfs(start)

for a, b in block:
    distance[a][b] = 9999

value = 0
zero_cnt = 0
for k in distance:
    for j in k:
        if j == 9999:
            continue
        if value < j:
            value = j
        if j == 0:
            zero_cnt += 1

if zero_cnt >= 1:
    print(-1)
else:
    print(value - 1)