n,m = map(int, input().split())
t = int(input())
time = n * 60 + m + t
h = time//60
if h>=24:
    m = time - h*60
    h = h - 24
else:
    m = time - h*60

print(h,m)