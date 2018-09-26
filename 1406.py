from sys import stdin

left = list(stdin.readline().rstrip())
right = []
TC = int(stdin.readline().rstrip())
for _ in range(TC):

    order = list(stdin.readline().split())

    if len(order) == 1:
        order = order[0]
    else:
        order, char = order[0], order[1]

    if order == 'L':
        if left:
            l = left.pop()
            right.append(l)
    elif order == 'D':
        if right:
            r = right.pop()
            left.append(r)
    elif order == 'B':
        if left:
            left.pop()
    elif order == 'P':
        left.append(char)

while left:
    check = left.pop()
    right.append(check)

result = ''
while right:
    result += right.pop()
print(result)