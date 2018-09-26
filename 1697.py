from collections import deque  # 큐
start, end = map(int, input().split())
visited = [0 for j in range(100000+1)]
def bfs(start,end):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        start = q.popleft()
        if start == end:
            print(visited[start]-1)
            break
        if start-1>=0 and visited[start-1]==0:
            visited[start-1] = visited[start]+1
            q.append(start-1)
        if start+1<=100000 and visited[start+1]==0:
            visited[start+1] = visited[start]+1
            q.append(start+1)
        if 2*start<=100000 and visited[start*2]==0:
            visited[start*2] = visited[start]+1
            q.append(start*2)
bfs(start, end)