n = int(input())
arr = [int(num) for num in input().split()]
dp = [x for x in arr]
for i in range(n):
    for j in range(i):
        if (arr[j]<arr[i]) and (dp[i] < (dp[j] + arr[i])):
            dp[i] = dp[j] + arr[i]
print(max(dp))