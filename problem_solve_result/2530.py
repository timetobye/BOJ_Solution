n, m, s = map(int, input().split())
t = int(input())
time = n * 60 ** 2 + m * 60 + s + t
h = time // 3600
if h >= 24:
    m = time - h * 3600
    h = h % 24

else:
    m = time - h * 3600

minute = m // 60
sec = m - minute * 60

print(h, minute, sec)