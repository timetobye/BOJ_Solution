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


if __name__ == "__main__":
    main()