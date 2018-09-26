n, k = map(int, input().split())
arr = []
for x in range(n):
    arr.append(int(input()))

dp = [0 for x in range(k + 1)]
dp[0] = 1

for i in arr:
    for j in range(1, k + 1):
        if i > j:
            continue
        else:
            dp[j] = dp[j - i] + dp[j]
print(dp[k])