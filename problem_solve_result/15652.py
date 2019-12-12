from itertools import combinations_with_replacement

n, m = [int(x) for x in input().split()]
arr = [int(x) for x in range(1, n+1)]

for i in combinations_with_replacement(arr, m):
    print(*i)