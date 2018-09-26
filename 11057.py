n = int(input())  # 손으로 써보면서 하면 짱이다.
dp = [[0 for x in range(10)] for x in range(n + 1)]  # 역시 쉬운 계단수 문제처럼 필요한 만큼만 배열을 만든다.
for j in range(0, 10):  # 0도 포함이니까 0부터 10까지 1로 지정
    dp[1][j] = 1
if n >= 2:
    for i in range(2, n + 1):
        for j in range(0, 10):  # 2부터 시작하는데 결국 누적합의 수열이므로 그것을 구현한다.
            dp[i][j] = sum(dp[i - 1][0:j + 1])  # 이건 그림을 그려보면 단번에 알 수 있다.

print(sum(dp[n]) % 10007)  # 계산한다.