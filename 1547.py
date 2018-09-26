n = int(input())

lst = [1,0,0]

for i in range(n):
    x, y= map(int, input().split())
    lst[x-1], lst[y-1] = lst[y-1], lst[x-1]

for i in range(3):
    if lst[i]:
        print(i+1)