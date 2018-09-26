n = int(input())
withdraw_time = list(map(int, input().split()))

withdraw_time.sort()  # 가장 적은 순서대로 합쳐져야 함

dp_sum = 0 #초기 값은 0 으로 설정

for i in range(n):
    dp_sum += sum(withdraw_time[:i+1])  # for문 한 번으로 해결
print(dp_sum)


'''
Legacy Code

n = int(input())
withdraw_time = list(map(int, input().split()))

withdraw_time.sort()  # 가장 적은 순서대로 합쳐져야 함

dp_sum = 0 #초기 값은 0 으로 설정

for i in range(n):
    check = 0   # 특정 순서까지의 합을 확인해주기 위한 변수
    for time in withdraw_time:   # 하나씩 꺼내오기
        dp_sum = dp_sum + time   # 누적 합 계산
        if check == i:           # i번째 사람의 i 번째 기다린거까지가 같으면 덧셈 멈춤
            break
        check +=1
print(dp_sum)                    #결과 호출

'''