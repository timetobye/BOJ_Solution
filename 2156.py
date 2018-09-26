n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

dp = [0 for x in range(n+1)]
if n>=1:
    dp[1] = grape[0]
if n>=2:
    dp[2] = dp[1] + grape[1]
if n >= 3:
    for i in range(3,n+1):
        dp[i] = max(dp[i-3] + grape[i-2]+grape[i-1], dp[i-1], dp[i-2] + grape[i-1])
print(max(dp))