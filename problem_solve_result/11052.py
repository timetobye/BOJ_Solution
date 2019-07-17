"""
dp[i] : i개 카드를 살 때의 최댓값

dp = [0 for x in range(n+1)]
dp[i] = max(dp[i], dp[i-j] + arr[j]

how to ...?
손으로 직접 써보면서 점화식을 유도해보았다.

1. 카드 1개를 사는 경우
카드 0개를 사는 경우의 최댓값 + 카드 1개를 살 때의 값
- dp[1] = dp[1-1] + arr[1]

2. 카드 2개를 사는 경우
카드 2개를 사는 경우의 최댓값 + 카드 0개를 살 때의 값
- dp[2] = dp[2-0] + arr[0]

카드 1개를 사는 경우의 최댓값 + 카드 1개를 살 때의 값
- dp[2] = dp[2-1] + arr[1]

카드 0개를 사는 경우의 최댓값 + 카드 2개를 살 때의 값
- dp[2] = dp[2-2] + arr[2]

dp[2] = max(2개를 사는 경우 중 최댓값)

3. 반복한다.

편의를 위해 arr에 insert(0,0) 처리를 하였다.

"""


n = int(input())
arr = [int(x) for x in input().split()]
arr.insert(0, 0)

dp = [0 for x in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + arr[j])

print(dp[n])