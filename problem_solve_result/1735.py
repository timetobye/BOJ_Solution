from math import gcd

arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

up = arr[0] * brr[1] + arr[1] * brr[0]
down = arr[1] * brr[1]

t = gcd(up,down)

print(up//t, down//t)