n, k = map(int, input().split())
dp =  [[1 for x in range(k+1)] for y in range(n+1)]
for i in range(k):
    for j in range(n+1):
        for p in range(j):
            dp[j][i+1] += dp[j-p][i]
print(dp[n][k-1] % 1000000000)