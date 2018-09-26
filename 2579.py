n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
dp = [0 for x in range(n+1)]
stair.insert(0,0)
if n >= 1:
    dp[1] = stair[1]
if n >= 2:
    dp[2] = stair[1] + stair[2]
if n >= 3:
    for i in range(3, n+1):
        dp[i] = max((dp[i-2] + stair[i]), (dp[i-3] + stair[i-1] + stair[i]))
print(dp[-1])