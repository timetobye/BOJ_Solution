from sys import stdin

n = int(input())
sequence = [x for x in range(1, n+1)]
required_sequence = []
for i in range(n):
    number = int(stdin.readline())
    required_sequence.append(number)

stack = []
element_number = 0
stack_status = []
value = 0
while True:
    if element_number > len(required_sequence)-1:
        break
    else:
        rs = required_sequence[element_number]
    if stack:
        if stack[-1] == rs:
            stack.pop()
            stack_status.append('-')
            element_number += 1
            ret = True
            continue

    if sequence:
        get = sequence.pop(0)
        stack.append(get)
        stack_status.append('+')
    else:
        ret = False
        break


if not ret:
    print('NO')
else:
    for i in stack_status:
        print(i)

'''
왜 맞았는지 모르겠다....
'''







