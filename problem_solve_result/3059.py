T = int(input())

for x in range(T):
    n = set(input())
    alpha = set()
    for x in range(65,91):
        alpha.add(chr(x))
    res = alpha - n
    cnt = 0
    for v in res:
        cnt += ord(v)
    print(cnt)