"""
시간 초과가 나서 참고하고 풀었습니다.
1. https://sexycoder.tistory.com/90

"""

import sys
from sys import stdin
from pprint import pprint
sys.setrecursionlimit(1000000)

m, n = [int(x) for x in stdin.readline().split()]

arr = [[0 for j in range(n+1)]]
for i in range(m):
    row = [int(x) for x in stdin.readline().split()]
    row.insert(0, 0)
    arr.append(row)

dp = [[-1 for j in range(n+1)] for i in range(m+1)]


def dfs(start_y, start_x):
    if (start_y == 1) and (start_x == 1):
        return 1

    if dp[start_y][start_x] == -1:
        dp[start_y][start_x] = 0

        points = [
            (start_y + 1, start_x),
            (start_y - 1, start_x),
            (start_y, start_x + 1),
            (start_y, start_x - 1)
        ]
        pprint(dp)
        for next_y, next_x in points:
            if (next_y >= 1) and (next_x >= 1) and (next_y <= m) and (next_x <= n):
                if arr[start_y][start_x] < arr[next_y][next_x]:
                    dp[start_y][start_x] += dfs(next_y, next_x)

    return dp[start_y][start_x]


dfs(m, n)
pprint(dp)
print(dp[m][n])






"""
legacy code : time limit
"""

# import sys
# from sys import stdin
# from pprint import pprint
# sys.setrecursionlimit(1000000)
#
# m, n = [int(x) for x in stdin.readline().split()]
#
# arr = []
# for i in range(m):
#     row = [int(x) for x in stdin.readline().split()]
#     arr.append(row)
#
# dp = [[0 for j in range(n)] for i in range(m)]
# visited = [[False for j in range(n)] for i in range(m)]
# dp[0][0] = 1
#
#
# def dfs(start_y, start_x):
#     visited[start_y][start_x] = True
#
#     points = [
#         (start_y + 1, start_x),
#         (start_y - 1, start_x),
#         (start_y, start_x + 1),
#         (start_y, start_x - 1)
#     ]
#
#     for next_y, next_x in points:
#         if next_y < 0 or next_x < 0 or next_y >= m or next_x >= n:
#             continue
#         if arr[start_y][start_x] <= arr[next_y][next_x]:
#             continue
#         """
#         방문을 했다면 기존 경로를 이용하며 되고
#         안 했다면 그대로 계속 탐색 하면 된다.
#         """
#         if not visited[next_y][next_x]:
#             dp[next_y][next_x] += 1
#             visited[next_y][next_x] = True
#
#             dfs(next_y, next_x)
#
#         else:
#             dp[next_y][next_x] += dp[start_y][start_x]
#
#
# dfs(0, 0)
# print(dp[m-1][n-1])
# pprint(dp)

