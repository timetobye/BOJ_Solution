"""
f(0) 이면 0 이 1개
f(1) 이면 1 이 1개
f(2) = f(1) + f(0) 이 되며, 0 이 1개, 1 이 1개
f(3) = f(2) + f(1) 이 되며, f(1) + f(0) + f(1) 이 되며 0 이 1개, 1이 2개

결국 n 에 해당하는 피보나치 값이 해답이 된다.
"""

from sys import stdin


def count_values(test_case_count):
    for _ in range(test_case_count):
        fibonacci_number = int(stdin.readline())

        if fibonacci_number == 0:
            print(1, 0)
            continue

        dp = [None for i in range(fibonacci_number + 1)]
        dp[0], dp[1] = 0, 1

        def calc_dp(n):
            if dp[n] is None:
                dp[n] = calc_dp(n-2) + calc_dp(n-1)

            return dp[n]

        calc_dp(fibonacci_number)
        print(dp[fibonacci_number - 1], dp[fibonacci_number])


if __name__ == "__main__":
    n = int(stdin.readline())
    count_values(n)


"""
legacy code

tc = int(input())
for _ in range(tc):
    n = int(input())

    # n == 0일 경우 print(0, 1)
    if n == 0:
        print(1, 0)
        continue
    dp = [None for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    # dp의 배열을 구하는 식
    def calc_dp(n):
        if dp[n] is None:
            dp[n] = calc_dp(n-1) + calc_dp(n-2)

        return dp[n]

    calc_dp(n)
    print(dp[n-1], dp[n])
"""
