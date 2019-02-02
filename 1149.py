n = int(input())
arr = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    arr.append(temp)

dp = [[0 for j in range(3)] for i in range(n)]

for i in range(n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

print(min(dp[n-1]))


"""
그리디로 한거라 안 풀린거였음

# n = int(input())
#
# color_cost_list = []
# for i in range(n):
#     temp = [int(x) for x in input().split()]
#     color_cost_list.append(temp)
#
# dp = [0 for i in range(n)]
#
#
# # k 번째 집을 찾는다.
# # 이전 단계에서 칠한 집의 index 번호를 넣는다.
# def find_color_list(k, idx_):
#     if idx_ == 0:
#         cost_ = min(color_cost_list[k][1], color_cost_list[k][2])
#         idx_ = color_cost_list[k].index(cost_)
#         return cost_, idx_
#     elif idx_ == 1:
#         cost_ = min(color_cost_list[k][0], color_cost_list[k][2])
#         idx_ = color_cost_list[k].index(cost_)
#         return cost_, idx_
#     elif idx_ == 2:
#         cost_ = min(color_cost_list[k][0], color_cost_list[k][2])
#         idx_ = color_cost_list[k].index(cost_)
#         return cost_, idx_
#
#
# for i in range(n):
#     if i == 0:
#         color_cost = min(color_cost_list[i])
#         dp[i] = color_cost
#         idx = color_cost_list[i].index(color_cost)
#         continue
#
#     cost, idx = find_color_list(i, idx)
#     dp[i] = dp[i - 1] + cost
#
# print(max(dp))
"""