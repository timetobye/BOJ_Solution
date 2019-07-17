from statistics import median
import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))


def one(lst):
    print(round(sum(lst) / len(lst)))


def two(lst):
    lst.sort()
    print(median(lst))


def three(lst):
    asdf = {}
    for x in lst:
        if x not in asdf:
            asdf[x] = 1
        else:
            asdf[x] += 1

    arr = []

    for y in asdf:
        if asdf[y] == max(asdf.values()):
            arr.append(y)

    if len(arr) == 1:
        print(arr[0])
    elif len(arr) >= 2:
        print(arr[1])


def four(lst):
    print(max(lst) - min(lst))


one(lst)
two(lst)
three(lst)
four(lst)