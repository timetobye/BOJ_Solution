"""
피타고라스 정리
가장 긴 변의 제곱 = 다른 두 변의 제곱의 합
if a=3, b=4, c=5라면
a^2 + b^2 = c^2
"""
from sys import stdin

while True:
    variable_list = [int(x) for x in stdin.readline().split()]
    variable_list.sort()

    a, b, c = variable_list

    if (a == 0) and (b == 0) and (c == 0):
        break
    elif (a**2 + b**2) == c**2:
        print("right")
    else:
        print("wrong")
