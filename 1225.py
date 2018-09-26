import sys

n, m = sys.stdin.readline().split()

n = list(n); m = list(m)

lst = 0
for i in n:
    lst += int(i) * sum(m)
print(lst)