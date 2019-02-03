n = int(input())
arr = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    arr.append(temp)

dp = [[0 for i in range(n)] for j in range(n)]
dp[0][0] = arr[0][0]


for j in range(1, n):
    k = len(arr[j])
    for i in range(k):
        if i == 0:
            dp[j][i] = dp[j-1][i] + arr[j][i]
        elif i == (len(arr[j])-1):
            dp[j][i] = dp[j-1][i-1] + arr[j][i]
        else:
            dp[j][i] = max(dp[j-1][i-1], dp[j-1][i]) + arr[j][i]

print(max(dp[n-1]))