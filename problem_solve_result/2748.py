"""
두 가지 방법으로 풀었음
"""


def fibo(n):
    cnt = 0
    f1 = 0
    f2 = 1
    while cnt < n:
        cnt += 1
        f1, f2 = f2, f1+f2
    return f1

n = int(input())

print(fibo(n))


"""
메모제이션 방법
2020.02.10
"""

def main():
    n = int(input())
    memo = [-1 for i in range(n+1)]
    memo[0], memo[1] = [0, 1]

    #memoization
    def fibo(n):
        if n <= 1:
            return memo[n]

        elif memo[n] != -1:
            return memo[n]

        else:
            memo[n] = fibo(n - 1) + fibo(n - 2)
            return memo[n]

    fibo(n)
    print(memo[n])


"""
더 간결하게 작성
2021.02.03
"""


def main_2():
    n = int(input())
    dp = [None for _ in range(n+1)]
    dp[0], dp[1] = [0, 1]

    def calc_dp(n):
        if dp[n] is None:
            dp[n] = calc_dp(n-1) + calc_dp(n-2)

        return dp[n]


    calc_dp(n)
    print(dp[n])


if __name__ == "__main__":
    main()


