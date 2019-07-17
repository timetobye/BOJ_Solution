"""
dp[j][i] : j를 만드는 데 i개를 사용하는 경우의 수

dp[j][i] = dp[j-0][i-1] + dp[j-1][i-1] + .... + dp[j - j][i-1]

example

20을 만드는 데 2개를 사용하는 경우의 수는

20를 만드는 데 1개를 사용하고 + 0을 더하는 경우의 수
+
19를 만드는 데 1개를 사용하고 + 1을 더하는 경우의 수
+
18를 만드는 데 1개를 사용하고 + 2를 더하는 경우의 수
+
.....
0을 만드는 데 1개를 사용하고 + 20을 더하는 경우의 수

for문을 사용해서 정리하면 될 듯

"""


from pprint import pprint
n, k = map(int, input().split())

dp = [[0 for i in range(k+1)] for j in range(n+1)]
for j in range(n+1):
    dp[j][1] = 1

if k >= 2:
    for i in range(2, k+1):  # 몇 개를 쓸 것인가?
        for j in range(n+1):  # 어떤 수에 대해 알아야 하는가?
            for p in range(j+1):
                # print(p)
                dp[j][i] += (dp[j-p][i-1])


print(dp[n][k] % 1000000000)











# n, k = map(int, input().split())
# dp =  [[1 for x in range(k+1)] for y in range(n+1)]
# for i in range(k):
#     for j in range(n+1):
#         for p in range(j):
#             dp[j][i+1] += dp[j-p][i]
# print(dp[n][k-1] % 1000000000)