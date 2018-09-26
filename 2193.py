n = int(input()) # 이진수를 print 해보니까 규칙이 있었다.
def prinary_number(n): # 1,1,2,3,5,....
    dp = [0,1,1] # 그래서 점화식으로 표현한 후 정리하였다.
    if n<=2:
        return dp[n]
    for i in range(3,n+1):
        dp.append(dp[i-2]+dp[i-1])
    return dp[n]

print(prinary_number(n))