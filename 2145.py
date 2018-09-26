while True:
    t = input()
    if t == '0':
        break
    while True:
        t = list(map(int,t))
        res = str(sum(t))
        if len(res) == 1:
            print(int(res))
            break
        t = res