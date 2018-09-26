from math import sqrt
import sys


def prime_num(num):
    if num > 1:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True
    else:
        return False


lst = []
for i in range(2, 100001):
    if prime_num(i):
        lst.append(i)

n = int(sys.stdin.readline())

for x in range(n):
    m = int(sys.stdin.readline())
    cnt = 0
    value = {}
    while True:
        if m % lst[cnt] == 0:
            m = m // lst[cnt]
            if lst[cnt] not in value:
                value[lst[cnt]] = 1
            else:
                value[lst[cnt]] += 1
        else:
            cnt += 1

        if m == 1:
            break
    for key, val in value.items():
        print(key, val)