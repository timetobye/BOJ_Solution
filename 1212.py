arr = [int(x) for x in input()][::-1] # 뒤집어서 계산
res = []
for i in range(len(arr)):
    for j in range(3):
        res.append(arr[i] % 2) # 나머지 값 구하고
        arr[i] = arr[i] // 2 # 몫만 구해서 대체하고
res = res[::-1] # 다시 뒤집기
cnt = 0
if len(res) == 1: # 혹시 하나만 들어올 경우
    pass
else:
    for i in range(len(res)):
        if res[0] == 0: # 가장 앞에 있는 값이 0이면 안 되니까
            res = res[1:]
        else:
            break
        cnt +=1
        if cnt == 2:
            break
res = [str(x) for x in res]
print(''.join(res))