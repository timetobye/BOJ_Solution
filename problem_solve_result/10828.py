from sys import stdin

n = int(stdin.readline())
stack = []

for i in range(n):
    order = stdin.readline().split()
    # print(f'stack is {stack}, order is {order}')
    if len(order) == 2:
        stack.append(order[1])
        continue

    if order[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
        continue

    if order[0] == 'size':
        print(len(stack))
        continue

    if order[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
        continue

    if order[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
