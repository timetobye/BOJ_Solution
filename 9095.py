TC = int(input())  # TC를 받는다

for x in range(TC):  # TC만큼 반복
    n = int(input())  # 정수 n 입력

    dp = [1, 2, 4]  # 기본적으로 설정된 값, 손으로 구했다.

    if n <= 3:  # 3이하면 패스
        pass
    else:
        for i in range(3, n):  # 3보다 클 경우
            result = dp[i - 3] + dp[i - 2] + dp[i - 1]  # 계속 호출해서 반복
            dp.append(result)  # dp를 채워나아간다.
    print(dp[n - 1])  # 0번부터 리스트는 시작이니까 1개 빼준다.