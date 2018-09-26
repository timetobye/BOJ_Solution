from itertools import combinations
from copy import deepcopy
from itertools import product
from collections import deque


def bfs(y, x, cnt):
    q = deque()
    q.append([y, x])
    visited[y][x] = False  # 더 이상 갈 필요 없게 만들고
    distance[y][x] = cnt
    while q:
        y, x = q.popleft()
        vector = [[y - 1, x], [y + 1, x], [y, x + 1], [y, x - 1]]
        for ny, nx in vector:
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if not visited[ny][nx] or data[ny][nx] == 1:
                continue
            q.append([ny, nx])
            visited[ny][nx] = False  # 새롭게 간 곳도 갈 필요 없게 만들고.
            distance[ny][nx] = cnt  # 큐 내에서는 값은 일정하게 유지 시킨다.


n, m = map(int, input().split())

arr = []
for x in range(n):
    arr.append(list(map(int, input().split())))

zero_point = []

for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] == 0:
            zero_point.append([x, y])  # 0 인 지점을 다 찾아두자. 기둥을 세워야 하니까!

result_box = []
for change_point in combinations(zero_point, 3):
    data = deepcopy(arr)  # 반복해서 쓸거니까 복사를 뜨고
    visited = [[True for j in range(m)] for i in range(n)]
    distance = [[0 for j in range(m)] for i in range(n)]

    for bx, by in change_point:  # 기둥 세울 3곳을 1로 변환해준다.
        data[bx][by] = 1

    for y in range(n):
        for x in range(m):
            if data[y][x] == 1:
                visited[y][x] = False  # 방문 기록에 대한 설정
                distance[y][x] = 1
            if data[y][x] == 2:
                visited[y][x] = False

    cnt = 999
    for b, a in product(range(n), range(m)):  # 구해서 정리하면 된다.
        if data[b][a] == 2:
            bfs(b, a, cnt)

    lst = []

    for v in distance:
        lst += v
    result_box.append(lst.count(0))

print(max(result_box))