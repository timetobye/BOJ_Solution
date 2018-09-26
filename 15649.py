from itertools import permutations
n, m = map(int, input().split())
lst = [x for x in range(1,n+1,1)]
for v in permutations(lst, m):
    v = list(map(str, v))
    v = " ".join(v)
    print(v)