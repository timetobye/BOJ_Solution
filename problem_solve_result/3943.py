import sys

TC = int(sys.stdin.readline()) # test_case
for _ in range(TC):
    dp = int(sys.stdin.readline())  # 시작 값
    max_value = dp # 시작 값이 가장 클 수도 있으니 max 지정
    while True:
        if dp == 1:
            break
        elif dp % 2 == 0:
            dp = dp // 2
        else:
            dp = (dp * 3) + 1
        if max_value < dp:   # max가 더 클 수도 있으니 값 교환
            max_value = dp
    print(max_value)