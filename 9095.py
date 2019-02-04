"""
dp[i] : 1,2,3을 이용해서 i를 나타낼 수 있는 경우의 수의 합

예를 들면

4를 만드는 방법은

1을 만드는 경우의 수 + 2를 만드는 경우의 수 + 3을 만드는 경우의 수의 합이다.

1을 만드는 경우의 수가 k 개 있으면 이 수가 4가 되려면 1에 3을 더해주면 4가 된다.

즉 1을 만드는 방법의 경우의 수눈 4를 만드는 경우의 수에 사용된다.

"""
import sys
sys.setrecursionlimit(10000000)

tc = int(input())


def calc_dp(i):
    if dp[i] is None:
        dp[i] = calc_dp(i-3) + calc_dp(i-2) + calc_dp(i-1)

    return dp[i]


for _ in range(tc):
    n = int(input())
    dp = [None for x in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4
    if n > 3:
        print(calc_dp(n))
    else:
        print(dp[n])













"""
# bottom-up method

TC = int(input())  # TC를 받는다

for x in range(TC):  # TC만큼 반복
    n = int(input())  # 정수 n 입력

    dp = [1, 2, 4]  # 기본적으로 설정된 값, 손으로 구했다.

    if n <= 3:  # 3이하면 패스
        pass
    else:
        for i in range(3, n):  # 3보다 클 경우
            result = dp[i - 3] + dp[i - 2] + dp[i - 1]  # 계속 호출해서 반복
            dp.append(result)  # dp를 채워나아간다.
    print(dp[n - 1])  # 0번부터 리스트는 시작이니까 1개 빼준다.
"""