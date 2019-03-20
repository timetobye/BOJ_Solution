n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(len(arr) - max(dp))