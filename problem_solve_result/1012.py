from collections import deque
T = int(input())
for _ in range(T):
    n, m, c = map(int, input().split())
    arr = [[0 for j in range(m)] for i in range(n)]  # 배추밭 생성
    start = []
    for x in range(c):                # 배추 위치 지정
        a,b = map(int, input().split())
        arr[a][b] = 1
        start.append([a,b])

    visited = [[False for j in range(m)] for i in range(n)] # 방문 지점에 대한 배열 설정
    distance = [[0 for j in range(m)] for i in range(n)]  # 거리에 대한 배열 설정
    def bfs(start):
        q =deque()
        for y,x in start:
            visited[y][x] = True  # 우선 배추 있는 곳은 다 True
            distance[y][x] = 1    # 배추 있는 곳은 기본적으로 1로 지정
        for temp in start:      #큐에 저장
            q.append(temp)
            while q:
                y, x = q.popleft()
                visited[y][x] = False   #다시 가는 것을 막기 위해 pop 한 지점
                adjacents = [[y-1,x], [y,x-1], [y+1, x], [y,x+1]]
                for next_y, next_x in adjacents:
                    if next_y<0 or next_y >=n or next_x <0 or next_x >= m:
                        continue
                    if not visited[next_y][next_x] or arr[next_y][next_x]==0:
                        continue
                    if distance[next_y][next_x] >1:
                        distance[y][x] +=1
                        continue
                    q.append([next_y,next_x])
                    visited[next_y][next_x] = True
                    distance[next_y][next_x] =  distance[y][x] + 1
    bfs(start)
    cnt = 0
    for z in distance:
        for h in z:
            if h ==1:
                cnt +=1
    print(cnt)