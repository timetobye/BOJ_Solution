"""
lcs 9251 번의 확장판이다.
dp 배열을 역추적하여 문자열을 찾아낸다.
while dp[m][n] != 0: # 0에 도달할 떄 까지 진행
    if dp[m][n] == dp[m-1][n]: 현재 위치의 값이 바로 위의 값과 같을 경우
        m -= 1
    elif dp[m][n] == dp[m][n-1]: 현재 위치의 값이 바로 옆의 값과 같을 경우
        n -= 1
    else:
        chase_string_list.append(s1[n-1]) # 대각선으로 이동!
        m -= 1
        n -= 1

참고로 dp 배열을 잡을 때
for j in range(m+1):
    for i in range(n+1):
        if j >= 1:
            dp[j][0] = 0
            continue
        dp[0][i] = 0

위와 같이 하면 계산이 무척 편리해진다.
손으로 직접 써보면 그걸 알 수 있다.
실제 계산은 (1,1)부터 되는 거지만...

참고
- https://2youngjae.tistory.com/77
"""


import sys
sys.setrecursionlimit(1000000)


def get_lcs_length(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[None for i in range(n+1)] for j in range(m+1)]

    for j in range(m+1):
        for i in range(n+1):
            if j >= 1:
                dp[j][0] = 0
                continue
            dp[0][i] = 0

    def calc_dp(m, n):
        if dp[m][n] is None:
            dp[m][n] = max(calc_dp(m - 1, n), calc_dp(m, n - 1))
            if s1[n - 1] == s2[m - 1]:
                dp[m][n] = max(dp[m][n], calc_dp(m - 1, n - 1) + 1)
        # pprint(dp)
        return dp[m][n]

    def chase_dp(m, n):
        chase_string_list = []
        while dp[m][n] != 0:
            if dp[m][n] == dp[m-1][n]:
                m -= 1
            elif dp[m][n] == dp[m][n-1]:
                n -= 1
            else:
                chase_string_list.append(s1[n-1])
                m -= 1
                n -= 1

        reversed_chase_string_list = reversed(chase_string_list)
        chase_string = "".join(reversed_chase_string_list)

        return chase_string

    return calc_dp(m, n), chase_dp(m, n)


def main():
    s1 = input()
    s2 = input()
    ret, chase = get_lcs_length(s1, s2)
    print(ret)
    print(chase)


if __name__ == "__main__":
    main()
