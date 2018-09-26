n = int(input())   # 자릿수별 숫자를 세서 시간 초과를 줄임
tp = len(str(n))

cnt = 0
for i in range(tp,0,-1):
    m = n - 10**(i-1) +1
    cnt += m * i
    n = n - m
print(cnt)

'''
import math   #시간 초과
n = int(input())
t = 0
for i in range(1,n+1):
    t += math.floor(math.log(i,10))+1
print(t)
'''