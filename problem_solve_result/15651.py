from itertools import product

n, m = [int(x) for x in input().split()]
arr = [int(x) for x in range(1, n+1)]

for i in product(arr, repeat=m):
    print(*i)