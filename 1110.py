k = int(input())
cnt = 0
t = 100
n = k
while True:
    if t == k:
        print(cnt)
        break
    else:
        if n >= 10:
            a = str(n)[0]
            b = str(n)[1]
            s = str(int(a)+int(b))
            if len(s) == 2:
                t = int(b + s[1])
            else:
                t = int(b + s)
        else:
            a = str(0)
            b = str(n)
            s = a+b
            t = int(s[1]*2)
        cnt +=1
        n = t