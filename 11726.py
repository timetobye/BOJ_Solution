n = int(input())

dp = [0 for x in range(n)]

if n == 1:
    dp[0]=1
elif n == 2:
    dp[1]=2
else:
    dp[0]=1
    dp[1]=2
    for i in range(2,n):
        dp[i] = ((dp[i-2] + dp[i-1]) % 10007)  # 점화식 세워주고, 마지막에 나누나 나누면서 넣으나 결론은 같다.

print(dp[n-1])