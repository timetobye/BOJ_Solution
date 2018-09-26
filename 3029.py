standard = list(map(int, input().split(':')))
time = list(map(int, input().split(':')))

if standard[0] == time[0] and standard[1] == time[1] and standard[2] == time[2]:
    res = '24:00:00'   # 문제를 똑바로 읽자. 최소 1초 기다리고 최대 24시간 기다린다고 함
else:
    if standard[0] > time[0]:
        time[0] += 24
    if standard[2] > time[2]:
        time[2] += 60
        time[1] -= 1
    if standard[1] > time[1]:
        time[1] += 60
        time[0] -= 1
    result = []
    for x in range(3):
        result.append(str(time[x] - standard[x]))
        if len(result[x]) ==1:
            result[x] = '0'+result[x]
    res = ":".join(result)
print(res)