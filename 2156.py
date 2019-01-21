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

"""
top-down method
"""

import sys

sys.setrecursionlimit(100000)

n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))

dp = [[None for j in range(3)] for i in range(n + 1)]
dp[0] = [0, 0, 0]
dp[1] = [0, wine[1], 0]


def calc_dp(n1, n2):
    if dp[n1][n2] is None:
        dp[n1][0] = max(calc_dp(n1 - 1, 0), calc_dp(n1 - 1, 1), calc_dp(n1 - 1, 2))
        dp[n1][1] = max(calc_dp(n1 - 2, 0), calc_dp(n1 - 2, 1), calc_dp(n1 - 2, 2)) + wine[n1]
        dp[n1][2] = calc_dp(n1 - 1, 1) + wine[n1]

    return dp[n1][n2]


calc_dp(n, 0)

print(max(dp[n]))