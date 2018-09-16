import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    t = int(sys.stdin.readline())
    lst.append(t)

lst.sort()
for i in lst:
    print(i)

'''
별다른 정렬 방법 없이
python의 sort()를 사용하였다.

파이썬 처음 배울 때 과제로 받았던,
오래전에 풀이한 내용이라 기록만 남긴다.
'''