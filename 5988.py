n = int(input())
for i in range(n):
    p = input()
    if int(p[-1]) % 2 == 1:
        print('odd')
    else:
        print('even')
