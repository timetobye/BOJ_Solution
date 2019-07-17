from math import sqrt
from math import ceil
import sys

n, m = map(int, sys.stdin.readline().split())
value = set((range(n, m + 1)))
for i in range(2, int(sqrt(m) + 1)):
    double = i ** 2
    value -= set(range(ceil(n / double) * double, m + 1, double))

print(len(value))