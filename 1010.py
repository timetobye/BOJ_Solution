def factorial(n):
    num = 1
    while n:
        num = num * n
        n = n - 1
    return num


TC = int(input())
for i in range(TC):
    west, east = map(int, input().split())
    value = factorial(east) / (factorial(west) * factorial(east-west)) # 파이썬은 정수형에는 제한이 없다
    print(int(value))



'''
legacy code

from math import ceil # 숫자 구조에 대해 공부가 필요

TC = int(input())
for i in range(TC):
    west, east = map(int, input().split())
    value = 1
    while True:
        value = value * (east/west)
        west -=1
        east -=1
        if west==0:
            break
    print(ceil(value))
'''
