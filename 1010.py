def get_bridge(n, m):
    # dp is None
    dp = [[None for j in range(m+1)] for i in range(m+1)]

    for i in range(m+1):
        dp[i][i] = 1
        dp[i][0] = 1

    def calc_dp(y, x):
        # Pascal's triangle, dynamic programming with top-down method
        if dp[y][x] is None:
            dp[y][x] = calc_dp(y-1, x) + calc_dp(y-1, x-1)

        return dp[y][x]

    return calc_dp(m, n)


def main():
    n = int(input())
    for i in range(n):
        west, east = map(int, input().split())
        print(get_bridge(west, east))


if __name__ == "__main__":
    main()


"""
def factorial(n):
    num = 1
    while n:
        num = num * n
        n = n - 1
    return num


TC = int(input())
for i in range(TC):
    west, east = map(int, input().split())
    value = factorial(east) / (factorial(west) * factorial(east-west)) # 파이썬은 정수형에는 제한이 없다
    print(int(value))
"""

"""
legacy code

from math import ceil # 숫자 구조에 대해 공부가 필요

TC = int(input())
for i in range(TC):
    west, east = map(int, input().split())
    value = 1
    while True:
        value = value * (east/west)
        west -=1
        east -=1
        if west==0:
            break
    print(ceil(value))
"""
