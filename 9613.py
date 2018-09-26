from math import gcd # 유클리드 호제법도 좋지만 간결하게 풀기 위해 math.gcd
from itertools import combinations # 손으로 구해본 후 조합을 이용해서 풀어야겠다고 판단
TC = int(input())
for _ in range(TC):
    sm = 0
    arr = [int(x) for x in input().split()]
    for a,b in combinations(arr[1:],2):
        sm += gcd(a,b)
    print(sm)