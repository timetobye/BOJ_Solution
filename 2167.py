"""
dp로의 접근 법을 고민하다가 결국 참고하였습니다.
https://jaemin8852.tistory.com/194

큰 것을 작게 나누어 계산하는 전형적인 dp인데 아직 부족해서 근본적인 개념을 못 이끌어 낸듯..

"""

from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]
arr = []
for i in range(n):
    temp = [int(x) for x in stdin.readline().split()]
    arr.append(temp)

k = int(stdin.readline())
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]


for _ in range(k):
    i, j, x, y = [int(x) for x in stdin.readline().split()]
    result_value = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
    print(result_value)

"""
legacy code : fail
"""

# from sys import stdin
#
#
# n, m =
#
# array = []
# for row in range(n):
#     array.append([int(x) for x in stdin.readline().split()])
#
# k = int(input())
#
# restriction_list = []
#
# for _ in range(k):
#     restriction_list.append([int(x)-1 for x in stdin.readline().split()])
#
#
# for rotation_number in range(k):
#     dp = 0
#     for p in range(n):
#         for q in range(m):
#             i, j, x, y = restriction_list[rotation_number]
#
#             if p < i or p > x or q < j or q > y:
#                 continue
#             else:
#                 dp += array[p][q]
#
#     print(dp)
