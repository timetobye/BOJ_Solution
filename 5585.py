back = 1000 - int(input()) # 거스름돈 총액
coin = [500, 100, 50 , 10 , 5, 1] # 교환 동전
cnt = 0 # 갯수
while back: # 교환할 돈이 없으면 종료한다.
    for x in coin: # coin 검색
        if (back // x) >= 1: #몫이 1이상이면 if문 실행
            back = back - x #금액 차감
            cnt +=1
            break  # for문 종료 while 다시 시작
print(cnt)