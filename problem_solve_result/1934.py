from math import gcd
n = int(input())

for i in range(n):
    p,q = map(int, input().split())
    t = int(p*q/gcd(p,q))
    print(t)