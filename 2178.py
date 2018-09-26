from collections import deque
n,m = map(int, input().split())
data = []
for x in range(n):
    arr = list(input())
    data.append(arr)

visited = [[False for j in range(m)] for i in range(n)]
distance = [[0 for j in range(m)] for i in range(n)]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    distance[y][x] = 1
    while q:
        y,x = q.popleft()
        adjacents = [[y-1,x], [y,x-1], [y+1,x], [y,x+1]]
        for next_y, next_x in adjacents:
            if next_y < 0 or next_y>= n or next_x< 0 or next_x>=m:
                continue
            if visited[next_y][next_x] or data[next_y][next_x] == '0':
                continue
            q.append([next_y, next_x])
            distance[next_y][next_x] = distance[y][x] + 1
            visited[next_y][next_x] = True
bfs(0,0)
print(distance[n-1][m-1])