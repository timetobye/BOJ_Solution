from math import sqrt


def prime_num(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


t = list(range(1, 123456 * 2 + 1))
lst = []
for x in t:
    if x % 2 == 1 or x == 2 and x != 1:
        if prime_num(x):
            lst.append(x)

while True:
    n = int(input())

    if n == 0:
        break

    cnt = 0
    for k in lst:
        if k > n and k <= 2 * n:
            cnt += 1
    print(len(cct))

'''
발견한 멋진 풀이

def primes_up_to(n: int) -> [int]: 
    seive = [False, False] + [True] * (n-1) 
    for (i, e) in enumerate(seive): 
        if e: 
            k = i * 2 
            while k <= n: 
                seive[k] = False 
                k += i 
    result = [x for (x, y) in enumerate(seive) if y ]
    return result

while True:
    n = int(input())
    if n == 0:
        break    
    m = n * 2
    result = set(primes_up_to(m)) - set(primes_up_to(n))
    new = list(range(n,m+1))
    print(len(list(set(new) & set(result))))
'''