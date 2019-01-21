# bottom-up

n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
dp = [0 for x in range(n+1)]
stair.insert(0,0)
if n >= 1:
    dp[1] = stair[1]
if n >= 2:
    dp[2] = stair[1] + stair[2]
if n >= 3:
    for i in range(3, n+1):
        dp[i] = max((dp[i-2] + stair[i]), (dp[i-3] + stair[i-1] + stair[i]))
print(dp[-1])

# top-down
n = int(input())
stair = [0]
for i in range(n):
    stair.append(int(input()))

# dp[i][j] : i번째 계단을 연속해서 j번 밟았을 때 얻을 수 있는 최대 점수

dp = [[None for j in range(3)] for i in range(n+1)]

dp[0] = [0, 0, 0]
dp[1][1] = stair[1]
dp[1][2] = 0

def calc_dp(n1, n2):
    if dp[n1][n2] is None:
        dp[n1][1] = max(calc_dp(n1-2, 1), calc_dp(n1-2, 2)) + stair[n1]
        dp[n1][2] = calc_dp(n1-1, 1) + stair[n1]

    return dp[n1][n2]

print(max(calc_dp(n, 1), calc_dp(n, 2)))