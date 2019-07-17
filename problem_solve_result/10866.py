from collections import deque
from sys import stdin

TC = int(stdin.readline())
q = deque([])

for x in range(TC):

    var = list(stdin.readline().split())

    if len(var) == 1:
        order = var[0]
    else:
        order, num = var[0], var[1]
    if order == 'push_front':
        q.appendleft(num)
    elif order == 'push_back':
        q.append(num)
    elif order == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)