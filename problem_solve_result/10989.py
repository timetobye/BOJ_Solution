import sys

n = int(sys.stdin.readline())

arr = [0 for i in range(10000 + 1)]
for i in range(n):
    value = int(sys.stdin.readline())

    arr[value] += 1

for i, value in enumerate(arr):
    if value == 0:
        continue

    for _ in range(value):
        print(i)
