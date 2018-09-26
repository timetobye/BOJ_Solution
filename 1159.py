import sys

n = int(sys.stdin.readline())
arr = []
for x in range(n):
    t = sys.stdin.readline()
    arr.append(t[0])

ct = list(set(arr))

lst = []
for y in ct:
    s = arr.count(y)
    if s >= 5:
        lst.append(y)

if len(lst) == 0:
    print("PREDAJA")
else:
    lst.sort()
    for z in lst:
        print(z, end="")