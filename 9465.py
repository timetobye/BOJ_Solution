TC = int(input())
for x in range(TC):
    n = int(input())
    data = []
    for _ in range(2):
        data.append(list(map(int, input().split())))
    dp = [[0 for x in range(3)] for y in range(n+1)]

    for i in range(1,n+1): # 최대 상태일 때 뜯지 않는 경우를 발생시킨다. 그리고 그 값이 1~2칸 뒤에 최대가 될 수 있다.
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) # 여태껏 발생한 값 중 큰 값 경로를 저장, 이번 경우에는 스티커를 떼지 않고 건너 뜀
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + data[0][i-1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + data[1][i-1]
    print(max(max(dp)))