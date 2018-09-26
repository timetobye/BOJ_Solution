from math import sqrt

n,m = map(int, input().split())

def is_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    else:
        return False

lst = []
for i in range(n,m+1):
    if is_prime(i):
        lst.append(i)

for j in lst:
    print(j)