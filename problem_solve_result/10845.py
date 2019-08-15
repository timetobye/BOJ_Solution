from sys import stdin
from collections import deque

n = int(stdin.readline())
que = deque([])

for i in range(n):
    order = stdin.readline().split()

    if len(order) == 2:
        que.append(order[1])
        continue

    if order[0] == 'pop':
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)
        continue

    if order[0] == 'size':
        print(len(que))
        continue

    if order[0] == 'empty':
        if len(que) != 0:
            print(0)
        else:
            print(1)
        continue

    if order[0] == 'front':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
        continue

    if order[0] == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)