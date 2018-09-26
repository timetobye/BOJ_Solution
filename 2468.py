from itertools import product
from collections import deque
from copy import deepcopy
n = int(input())
brr = []
for x in range(n):
    brr.append(list(map(int, input().split())))

mx_high = max(max(brr))   # 최대 높이를 정한다.
mx_temp = 0

for z in range(1,mx_high+1):  # 최대 높이까지 반복한다.
    arr = deepcopy(brr)       # 반복적으로 사용할 거라 copy를 이용하여 반복 사용할 수 있게 설정하였다.
    visited = [[False for j in range(n)] for i in range(n)]
    distance = [[0 for j in range(n)] for i in range(n)] #방문 할 수 있으면 계속 같은 숫자로 가면 된 다.
    for y in range(n):
        for x in range(n):
            if arr[y][x] < z:
                arr[y][x] = 0
            else:
                arr[y][x] = 1                            # 숫자를 0,1로 바꿔서 비교해주었다. 굳이 안해도 될지도
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
                visited[ny][nx] = False   # 방문 했으니 이제 갈 일 없도록
                distance[ny][nx] = cnt

    temp = 0
    cnt = 1
    for b, a in product(range(n), range(n)):  # 주명님이 알려주신 방법 참고해서 구현
        if visited[b][a]:                     # 해당 좌표가 True이면 if문이 작동
            bfs(b,a,cnt)
            cnt +=1
            temp +=1
    if temp > mx_temp:                        # 최대값 비교 후 갱신
        mx_temp = temp
print(mx_temp)