T = int(input())
for x in range(T):
    n = int(input())
    door = [False for x in range(n)]
    cnt = 1
    for k in range(n): # 라운드 번호
        for j in range(n): #각 방을 순회
            if (j+1) % cnt == 0:
                if door[j] == True:
                    door[j] = False
                else:
                    door[j] = True
        cnt +=1
        temp = 0
        for z in door:
            if z:
                temp +=1

    print(temp)