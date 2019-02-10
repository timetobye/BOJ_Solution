n = int(input())

dp = [0 for x in range(n+1)]
dp[0] = 1
dp[1] = 3

if n >= 2:
    dp[2] = 7

if n >= 3:
    for i in range(3, n+1):
        dp[i] = dp[i - 2] + (dp[i - 1] * 2)
        dp[i] = dp[i] % 9901

print(dp[n])
