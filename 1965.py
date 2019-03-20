from bisect import bisect_left


n = int(input())
arr = [int(x) for x in input().split()]
arr.insert(0, 0)

dp = []

for i in range(1, n + 1):
    if (not dp) or (dp[-1] < arr[i]):
        dp.append(arr[i])
    else:
        dp[bisect_left(dp, arr[i])] = arr[i]

print(len(dp))