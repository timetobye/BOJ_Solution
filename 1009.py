TC = int(input())
for _ in range(TC):
    a, b = map(int, input().split())
    a = (a % 10)
    if a ==0 or a == 1 or a == 5 or a == 6:
        if a == 0:
            print(10)
            continue
        else:
            print(a)
            continue
    t = 1
    arr = []
    for i in range(b):
        t = (t * a) % 10
        if t in arr:
            break
        arr.append(t)
    print(arr[b%(len(arr)) -1])