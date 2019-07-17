p,q,r = map(int, input().split())
if q>=r:
    print(-1)
else :
    print(int(p/(r-q) +1))