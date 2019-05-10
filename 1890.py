"""
dp[start_x][start_y] = 0이면 continue
start_x ==0 and start_y ==0이면 continue

시간초과를 벗어나기 위해서는 모든 곳을 다 볼 필요가 없다.
이전에 본 값을 가져와서 반복 사용하면 된다.
"""


from sys import stdin


def jump_matrix(n, arr):
    dp = [[0 for j in range(n)] for i in range(n)]
    dp[0][0] = 1

    for start_x in range(n):
        for start_y in range(n):

            if dp[start_x][start_y] == 0:
                continue

            if (start_x == (n - 1)) and (start_y == (n - 1)):
                continue

            jump_value = arr[start_x][start_y]

            end_x = jump_value + start_x
            end_y = jump_value + start_y

            if end_x < n:
                dp[end_x][start_y] += dp[start_x][start_y]

            if end_y < n:
                dp[start_x][end_y] += dp[start_x][start_y]

    return dp[n-1][n-1]


def main():
    n = int(input())
    arr = []

    for i in range(n):
        component = [int(x) for x in stdin.readline().split()]
        arr.append(component)

    res = jump_matrix(n, arr)

    print(res)


if __name__ == "__main__":
    main()






"""
legacy code

q를 이용해서 풀었으나 실패!

6%에서 시간 초과가 걸렸다.

"""


# from sys import stdin
# from collections import deque
# from pprint import pprint
#
# n = int(input())
#
# arr = []
#
# for i in range(n):
#     component = [int(x) for x in stdin.readline().split()]
#     arr.append(component)
#
# dp = [[0 for j in range(n)] for i in range(n)]
# dp[0][0] = 1
#
# q = deque([[0, 0]])
#
# while q:
#     start_x, start_y = q.pop()
#
#     if (start_x == (n-1)) and (start_y == (n-1)):
#         continue
#
#     jump_value = arr[start_x][start_y]
#
#     end_x = jump_value + start_x
#     end_y = jump_value + start_y
#
#     if end_x < n:
#         dp[end_x][start_y] += dp[start_x][start_y]
#
#         q.append([end_x, start_y])
#
#     if end_y < n:
#         dp[start_x][end_y] += dp[start_x][start_y]
#
#         q.append([start_x, end_y])
#
# print(dp[n-1][n-1])
# pprint(dp)

