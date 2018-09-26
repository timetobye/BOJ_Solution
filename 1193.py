n = int(input())
t = 1
while True:
    s = int(t*(t+1)/2)
    k = int((t+1)*(t+2)/2)
    if n == 1:
        print("%d/%d" % (1, 1))
        break
    elif n > s and n <= k:
        if (t%2) == 0:
            cnt = n-s
            top = t-cnt+2
            print("%d/%d" % (top, cnt))
        elif (t%2) == 1:
            cnt = n-s
            top = t-cnt+2
            print("%d/%d" % (cnt, top))
        break
    else:
        t += 1