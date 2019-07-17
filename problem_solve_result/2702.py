from math import gcd

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    g = gcd(a,b)
    G = int(a*b/g)
    print(G, g)