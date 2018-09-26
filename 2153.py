from math import sqrt
n = input()

lst = list(n)
alpha_lower = [chr(x) for x in range(97,123)]
alpha_upper = [chr(x) for x in range(65,91)]
alpha = alpha_lower + alpha_upper

cnt = 0
for i in lst:
    cnt += (alpha.index(i)+1)

temp = 0
if cnt >1:
    for i in range(2,int(sqrt(cnt))+1):
        if cnt % i == 0:
            temp +=1
            break
elif cnt == 1:   #1도 편의상 소수로 지정(문제 내 설정)
    temp = 0
else:
    temp +=1
if temp==0:
    print("It is a prime word.")
elif temp > 0:
    print("It is not a prime word.")