from math import sqrt
from sys import stdin
prime = [int(x) for x in range(1000001)] # 체를 구현
prime[1] = 0
for p in range(2,int(sqrt(1000000)+1)):
    if prime[p] != 0:
        for q in range(2*p, 1000000, p):
            prime[q] = 0

while True: # 모든 숫자를 확인 할 필요는 없다.
    n = int(stdin.readline())
    cnt = 0
    if n == 0:
        break
    for i in range(2,len(prime)//2 +1): # 절반만 확인해도 된다. 어차피 가장 작은 수 + 가장 큰 수의 조합이기 때문
        if prime[i] and (prime[n-i]):
            print("{} = {} + {}".format(n, prime[i], prime[n-i]))
            cnt +=1
            break
    if cnt == 0: # 문제를 잘 읽어보면 이건 굳이 안 넣어도 될 것 같다.
        print("Goldbach's conjecture is wrong.")