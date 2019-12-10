from itertools import combinations

n, m = [int(x) for x in input().split()]
arr = [int(x) for x in range(1, n+1)]

for i in combinations(arr, m):
    print(*i)