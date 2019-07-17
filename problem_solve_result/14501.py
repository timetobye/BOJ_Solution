"""
dp[i]를 아래와 같이 정의 하였다.
 - dp[i] = i 일 까지 얻을 수 있는 최대 금액

정의는 했으나 실력 부족으로 코드 전개를 할 수 없었다.

아래의 주소를 참고하여 다시 접근하였다.

https://bcp0109.tistory.com/8

아래서부터 올라가는 방식으로 접근하는 것보다 위에서 아래로 접근하는 방식으로 하니까

더 쉽게 이해 할 수 있었다.
"""

n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])

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
