n = int(input())
arr = [int(num) for num in input().split()]
dp = [0 for x in range(n)]

for i in range(n):
    print('-------------------')
    print(dp[i-1])
    dp[i] = max(arr[i], dp[i-1] + arr[i])
print(max(dp))