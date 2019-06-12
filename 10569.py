from sys import stdin

n = int(stdin.readline())

for i in range(n):
    v, e = [int(x) for x in stdin.readline().split()]
    x = 2 - v + e
    print(x)
