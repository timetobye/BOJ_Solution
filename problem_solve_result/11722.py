n = int(input())
arr = [int(num) for num in input().split()[::-1]]
dp = [1 for x in range(n)]
for i in range(n):
    for j in range(i):
        if (j<i) and (arr[j]<arr[i]):
            result = dp[j] + 1
            if result > dp[i]:
                dp[i] = result
print(max(dp))