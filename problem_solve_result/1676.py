"""
너무 어렵게 생각하지 말자
쉽게 접근 했었는데, 조금만 더 고민했으면 풀었을 문제이다.
"""


def solution(n):
    number = 5
    count = 0

    while n >= number:
        count += n // number
        number = number * 5

    return count


if __name__ == "__main__":
    n = int(input())
    res = solution(n)
    print(res)




"""
legacy code - 1

import sys

sys.setrecursionlimit(1000000)


def solution(n):
    dp = [None for _ in range(n + 1)]

    def calc_dp(n, divided_number):
        if (n % divided_number) != 0:
            return 0
        elif dp[n] is not None:
            return dp[n]
        else:
            result = calc_dp(n // divided_number, divided_number) + 1
            return result

    answer = 0
    for i in range(1, 1 + n):
        dp[i] = calc_dp(i, 5)
        if dp[i] == 0:
            continue
        answer += dp[i]

    return answer


if __name__ == "__main__":
    n = int(input())
    result = solution(n)
    print(result)



legacy code - 2

n = int(input())
s = 1
count = 0
h = []

if n == 0 :
    count = 0

if n > 0:
    while n > 1:
        s = s * n
        n = n -1
    s= str(s)
    for i in range(len(s)):
        h.append(int(s[-(i+1)]))
        count = count + 1
        if sum(h) != 0:
            count -= 1
        else:
            True
        
print(count)

"""