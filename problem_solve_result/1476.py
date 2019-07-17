e,s,m = map(int, input().split())
n = 1
while True:
    p = n%15; q= n%28; r= n%19;
    if p == 0:
        p = 15
    if q == 0:
        q = 28
    if r == 0:
        r = 19
    if p == e and q == s and r == m:
        print(n)
        break
    else:
        n += 1