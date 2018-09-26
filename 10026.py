# 유기농 배추, 전단지붙이지, 안전 영역 문제와 유사

from itertools import product
from collections import deque
from copy import deepcopy

n = int(input())
brr = []
for x in range(n):
    brr.append(list(input()))

result = []
for twice in range(2):  # 한 번만 비교하면 되니까
    arr = deepcopy(brr)
    if twice == 1:
        for y in range(n):
            for x in range(n):
                if arr[y][x] == 'G':
                    arr[y][x] = 'R'

    distance = [[0 for j in range(n)] for i in range(n)]
    visited = [[True for j in range(n)] for i in range(n)]


    def bfs(y, x, cnt):
        q = deque()
        q.append([y, x])
        visited[y][x] = False
        distance[y][x] = cnt
        while q:
            y, x = q.popleft()
            vector = [[y - 1, x], [y + 1, x], [y, x + 1], [y, x - 1]]
            for ny, nx in vector:
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if (arr[y][x] != arr[ny][nx]) or visited[ny][nx] == False:
                    continue
                q.append([ny, nx])
                visited[ny][nx] = False
                distance[ny][nx] = cnt


    temp = 0
    cnt = 1
    for b, a in product(range(n), range(n)):  # 구해서 정리하면 된다.
        if visited[b][a]:
            bfs(b, a, cnt)
            cnt += 1
            temp += 1
    result.append(temp)

for x in result:
    print(x, end=" ")