n, m = map(int, input().split())

lst = list(range(2, n + 1))
arr = []
while True:
    if len(lst) == 0:
        break
    t = min(lst)
    arr += [x for x in lst if (x % t) == 0]
    lst = [x for x in lst if (x % t) != 0]

print(arr[m - 1])