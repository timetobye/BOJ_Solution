from math import sqrt


def prime_num(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


lst = []

n = int(input())
m = int(input())

for i in range(n, m + 1):
    if prime_num(i):
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))