TC = int(input())
for x in range(TC):
    n = int(input())
    dp = [0,1,1,1,2,2]
    if n <= 5:
        print(dp[n])
    else:
        for i in range(6,n+1):
            res = dp[i-1] + dp[i-5]
            dp.append(res)
        print(dp[n])