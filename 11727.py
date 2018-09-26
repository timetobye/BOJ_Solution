n = int(input())

dp = [0 for x in range(n+1)]
dp[0] = 1
dp[1] = 3
if n<=1:
    pass
else:
    for i in range(2,n):
        dp[i] = ((2*dp[i-2] + dp[i-1]) % 10007)
print(dp[n-1])

'''

Legacy Code
n = int(input())

dp = [1,3]

if n<=1:
    pass
else:
    for i in range(2,n):
        result = ((2*dp[i-2] + dp[i-1]) % 10007)
        dp.append(result)
print(dp[n-1])

'''