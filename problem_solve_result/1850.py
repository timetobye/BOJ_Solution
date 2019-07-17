from math import gcd
n, m = map(int, input().split())
p = gcd(n,m)
t = '1'*p

print(t)