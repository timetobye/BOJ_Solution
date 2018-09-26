n = list(input())
temp = 0


if len(n) == 1:   #일의 자리 수는 변환 과정이 없이 바로 계산이 가능하다.
    n = n
else:
    while True:
        n = list(str(sum(list(map(int, n)))))
        temp +=1
        if len(n) == 1:
            break

print(temp)

if int(n[0])%3 == 0:
    print("YES")
else:
    print("NO")