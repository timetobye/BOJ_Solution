from math import sqrt

n = int(input())
dp = [x+1 for x in range(n)]
dp.insert(0,0)
for i in range(n+1):
    for j in range(1,int(sqrt(i))+1):
        if dp[i] > (dp[i - j*j] +1):
            dp[i] = (dp[i - j*j] +1) # 제곱수일 경우 그냥 0 +1이다.자기 자신 한 개가 최소니까.
print(dp[n])