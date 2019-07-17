"""
1. n, m입력을 받습니다.
2. 계산 편의를 위해 배열에 0을 추가 시켜줍니다.

[[0, 0, 0, 0, 0]
[0]
[0]
[0]
[0]
]

3. 다른 입력 값을 arr와 합쳐줍니다. 리스트의 덧셈은 리스트 arr를 끝으로 추가해줍니다.
4. dp[j][i]에 대한 정의는 j,i에서 가질 수 있는 사탕의 최댓값입니다.
5. dp 배열도 arr와 동일하게 구성합니다.
6. 각 j, i에서 위, 왼쪽, 대각선(dp[j-1][i-1]) 방향 중 최대인 값을 가져와서 저장합니다.
이전의 값 중 최댓값만을 저장하기 때문에 이전 최댓값 + 현재arr의 값이 유지됩니다.
7. 정답을 출력합니다.

"""

n, m = map(int, input().split())
arr = [[0] for x in range(n+1)]
arr[0] = arr[0] + [0 for x in range(m)]

for i in range(1, n+1):
    arr[i] = arr[i] + [int(x) for x in input().split()]

dp = [[0 for i in range(m+1)] for j in range(n+1)]
dp[1][1] = arr[1][1]

for j in range(1, n+1):
    for i in range(1, m+1):
        dp[j][i] = arr[j][i] + max(dp[j-1][i-1], dp[j-1][i], dp[j][i-1])

print(dp[n][m])

