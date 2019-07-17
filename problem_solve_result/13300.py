import math

n, m = map(int, input().split())

lst = []
for k in range(n):
    t = list(input().split())
    lst.append(t)

cnt = 0
for p in range(1, 7):
    arr = []
    for i in range(len(lst)):
        if lst[i][1] == str(p):
            arr.append(lst[i])
    girl = [];
    boy = [];
    for j in arr:
        if j[0] == '0':
            girl.append(j)
        else:
            boy.append(j)
    girl_cnt = len(girl)
    boy_cnt = len(boy)

    cnt += math.ceil(girl_cnt / m)
    cnt += math.ceil(boy_cnt / m)
print(cnt)