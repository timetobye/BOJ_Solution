dp = [0,0] # 시작 위치는 0,0으로 설정, 동전 문제 푸는 것과 유사하게 접근함

n = int(input())

for i in range(2,n+1): # 2부터 n 까지 수열 정리
    temp = []
    temp.append(dp[i-1]+1) # 1차이는 무조건 되니까 넣고
    if i % 2 == 0:
        temp.append(dp[i//2]+1) # 2로 나누어 떨어지는지는 확인
    if i % 3 == 0:
        temp.append(dp[i//3]+1) # 3으로 나누어 떨어지는지도 확인
    dp.append(min(temp)) # 그 중 최소값
print(dp[n]) # n번째 출력

'''
참고한 코드

a = int(input())
count = 0
minimum=[a]
def cal(a):
    list = []
    for i in a:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return list
 
while True:
    if a == 1:
        print(count)
        break
    
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count +=1
    if min(minimum) == 1:
        print(count)
        break
'''