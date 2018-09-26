from math import ceil
n,a,b = map(int, input().split())
cnt = 1
while True:
    a_temp = ceil(a/2)   # 1,2 의 경우 새롭게 올라가는 번호는 1이 된다.
    b_temp = ceil(b/2)   # 이를 응용하면 모든 올라가는 번호를 새롭게 부여할 수 있다.
    gap = abs(a_temp - b_temp)
    if gap == 0:        # 그리고 두개가 같아지면 같은 라운드라고 볼 수 있다.
        print(cnt)
        break
    else:
        cnt +=1
        a = a_temp
        b = b_temp