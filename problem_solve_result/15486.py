from sys import stdin

n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in stdin.readline().split()])

# i + 1을 해결하기 위해 임의로 부여
arr.append([0, 0])

dp = [0 for x in range(n + 1)]

for i in range(n-1, -1, -1):
    # 상담 가능한 일자를 넘어가면 안 되므로 설정
    if i + arr[i][0] <= n:
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
