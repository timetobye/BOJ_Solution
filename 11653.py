# from math import sqrt
#
# prime = [int(x) for x in range(10000001)]
# prime[1] = 0
# for p in range(2, int(sqrt(10000000))+1):
#     if prime[p] != 0:
#         for q in range(2*p,10000000, p):
#             prime[q] = 0
#
# prime = [int(x) for x in prime if x !=0]
#
# num = int(input())
# idx = 0
# while True:
#     if num % prime[idx] == 0:
#         print(prime[idx])
#         num = num // prime[idx]
#     else:
#         idx +=1
#     if num == 1:
#         break

'''
소수 배열을 만든 후에 접근하려고 했으나
시간 초과를 받았다.

단순하게 1씩 증가시켜서 접근을 한 후 AC 받았다.
가끔은 단순하게 접근하는 것도 하나의 방법이 된다.

'''


num = int(input())
idx = 2
while True:
    if num % idx == 0:
        print(idx)
        num = num // idx
    else:
        idx +=1
    if num == 1:
        break