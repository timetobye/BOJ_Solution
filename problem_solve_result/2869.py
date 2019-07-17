import sys

a,b,v = map(int, sys.stdin.readline().split())

if (v-b)%(a-b) == 0:
    temp = (v-b)//(a-b)
else:
    temp = (v-b)//(a-b) + 1
print(temp)


'''
a,b,v = map(int, input().split())  #시간 초과

dis = 0
day = 0
while dis < v:
    dis += a
    if dis >= v:
        day += 1
        break
    dis -= b
    day += 1
print(day)
'''