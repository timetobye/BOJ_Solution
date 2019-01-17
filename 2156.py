"""
1차원 배열
"""

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

dp = [0 for x in range(n+1)]
if n >= 1:
    dp[1] = grape[0]
if n >= 2:
    dp[2] = dp[1] + grape[1]
if n >= 3:
    for i in range(3,n+1):
        dp[i] = max(dp[i-3] + grape[i-2]+grape[i-1], dp[i-1], dp[i-2] + grape[i-1])
print(max(dp))

"""
2차원 배열
"""

n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))

dp = [[0 for i in range(3)] for x in range(n + 1)]
dp[1][1] = wine[1]

for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])  # 안 마실 때
    dp[i][1] = max(dp[i - 2][0], dp[i - 2][1], dp[i - 2][2]) + wine[i]  # 1잔 연속 마실 때
    dp[i][2] = dp[i - 1][1] + wine[i]  # 2잔 연속 마실 때

print(max(dp[n]))

