# 유기농 배추, 안전영역과 모든 개념이 동일하다. 출력 부분에서 요구하는 것만 다르다.

from itertools import product
from collections import deque
n = int(input())
arr = []
for x in range(n):
    arr.append(list(input()))

visited = [[False for j in range(n)] for i in range(n)]
distance = [[0 for j in range(n)] for i in range(n)]
for y in range(n):
    for x in range(n):
        if arr[y][x] == '1':
            visited[y][x] = True

def bfs(y,x,cnt):
    q = deque()
    q.append([y,x])
    visited[y][x] = False
    distance[y][x] = cnt
    while q:
        y,x = q.popleft()
        vector = [[y-1,x],[y+1,x],[y,x+1],[y,x-1]]
        for ny, nx in vector:
            if ny < 0 or ny >=n or nx < 0 or nx >= n:
                continue
            if not visited[ny][nx]:
                continue
            q.append([ny,nx])
            visited[ny][nx] = False   # 방문한 집은 갈 필요가 없다.
            distance[ny][nx] = cnt   # 큐 내에서는 단지의 값은 항상 동일


temp = 0
cnt = 1
for b, a in product(range(n), range(n)): # 구해서 정리하면 된다.
    if visited[b][a]:
        bfs(b,a,cnt)
        cnt +=1
        temp +=1
print(temp)
lst = []
for v in distance:
    lst += v
cnt = 0
brr = []
for v in range(1,temp+1):
    brr.append(lst.count(v))

brr.sort()
for x in brr:
    print(x)