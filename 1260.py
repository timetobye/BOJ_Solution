n, m, v = map(int, input().split())
data = [[] for i in range(n + 1)]

for x in range(m):
    p, q = map(int, input().split())
    data[p].append(q)
    data[q].append(p)

for j in data:  # 리스트 안의 리스트를 정렬해야 한다. 잊지 말 것!
    j.sort()

visited = [False for i in range(n + 1)]


def dfs(u):
    print(u, end=" ")
    visited[u] = True
    for x in data[u]:
        if not visited[x]:
            dfs(x)


from collections import deque

bfs_visited = deque([])
bfs_temp = deque([])


def bfs(u):
    bfs_visited.append(u)
    while bfs_visited:
        for x in data[bfs_visited[0]]: # 나중에 여쭤보니 in list 형식은 시간을 많이 잡아 먹는다고 한다.
            if x not in bfs_visited + bfs_temp:
                bfs_visited.append(x)
        bfs_temp.append(bfs_visited.popleft())
    for y in bfs_temp:
        print(y, end=" ")


dfs(v)
print() # 줄바꿈 처리
bfs(v)