<<<<<<< HEAD
from bisect import bisect_left


n = int(input())
arr = [int(x) for x in input().split()]
arr.insert(0, 0)

dp = []

for i in range(1, n + 1):
    if (not dp) or (dp[-1] < arr[i]):
        dp.append(arr[i])
    else:
        dp[bisect_left(dp, arr[i])] = arr[i]

print(len(dp))
||||||| merged common ancestors
=======
"""
n^2 풀이 방식
전형적인 LIS 문제
"""


# n = int(input())
# arr = [int(x) for x in input().split()]
# arr.insert(0, 0)
#
# dp = [1 for x in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(1, i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))


"""
nlog * n 으로 풀기
"""

from bisect import bisect_left


n = int(input())
arr = [int(x) for x in input().split()]
arr.insert(0, 0)

dp = []

for i in range(1, n + 1):
    if (not dp) or (dp[-1] < arr[i]):
        dp.append(arr[i])
    else:
        dp[bisect_left(dp, arr[i])] = arr[i]

print(len(dp))
>>>>>>> efd0c3f840f861aa73246995377837bd58f76b77
