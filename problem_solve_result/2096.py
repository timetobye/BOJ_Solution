"""
본질적으로는 RGB거리 문제와 동일하다.
https://www.acmicpc.net/problem/1149

다만 메모리 부분에서 문제가 발생하는데 그건 아래의 링크를 참고하였다.
https://yabmoons.tistory.com/173

결국 dp에 모든 결과를 저장 할 필요 없이 이전 단계와 현재 단계만 저장하고
계속 값을 재활용하면서 진행하면 결국 dp는 2개의 열만 가지고도 문제를 이어 나갈 수 있다.

그리고 python의 경우 input 대신 sys.stdin.readline()을 사용하면 훨씬 빠르다.

dp[1][1] = min(dp[1][0] - score_arrays[j][0], dp[0][2]) + score_arrays[j][1]

된 부분이 있는데 이전 단계의 dp[1][0]에서 나온 결과를 재활용한 것이다. 조금이라도 있는 걸 쓰는 자세.
"""


import sys


def get_value(n, score_arrays, type):
    dp = [[0 for i in range(3)] for j in range(2)]

    if type == 'min':

        # dp_min_case
        for j in range(n + 1):
            dp[1][0] = min(dp[0][0], dp[0][1]) + score_arrays[j][0]
            dp[1][1] = min(dp[1][0] - score_arrays[j][0], dp[0][2]) + score_arrays[j][1]
            dp[1][2] = min(dp[0][1], dp[0][2]) + score_arrays[j][2]

            dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

        min_value = min(dp[1])
        
        return min_value
    
    else:

        # dp_max_case
        for j in range(n + 1):
            dp[1][0] = max(dp[0][0], dp[0][1]) + score_arrays[j][0]
            dp[1][1] = max(dp[1][0] - score_arrays[j][0], dp[0][2]) + score_arrays[j][1]
            dp[1][2] = max(dp[0][1], dp[0][2]) + score_arrays[j][2]

            dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

        max_value = max(dp[1])

        return max_value


def main():
    n = int(input())
    score_arrays = [[0, 0, 0]]

    for i in range(n):
        score_array = [int(x) for x in sys.stdin.readline().split()]
        score_arrays.append(score_array)

    min_score = get_value(n, score_arrays, 'min')
    max_score = get_value(n, score_arrays, 'max')

    print(max_score, min_score)


if __name__ == "__main__":
    main()



"""
legacy code
"""
#
#
# n = int(input())
# score_arrays = [[0, 0, 0]]
#
# for i in range(n):
#     score_array = [int(x) for x in input().split()]
#     score_arrays.append(score_array)
#
# dp_min = [[0 for i in range(3)] for j in range(n+1)]
# dp_max = [[0 for i in range(3)] for j in range(n+1)]
#
# # dp_min_case
# for j in range(n+1):
#     dp_min[j][0] = min(dp_min[j - 1][0], dp_min[j - 1][1]) + score_arrays[j][0]
#     dp_min[j][1] = min(dp_min[j - 1][0], dp_min[j - 1][1], dp_min[j - 1][2]) + score_arrays[j][1]
#     dp_min[j][2] = min(dp_min[j - 1][1], dp_min[j - 1][2]) + score_arrays[j][2]
#
# min_value = min(dp_min[n])
# print(min_value)
#
# # dp_max_case
# for j in range(n+1):
#     dp_max[j][0] = max(dp_max[j - 1][0], dp_max[j - 1][1]) + score_arrays[j][0]
#     dp_max[j][1] = max(dp_max[j - 1][0], dp_max[j - 1][1], dp_max[j - 1][2]) + score_arrays[j][1]
#     dp_max[j][2] = max(dp_max[j - 1][1], dp_max[j - 1][2]) + score_arrays[j][2]
#
# max_value = max(dp_max[n])
# print(max_value)
