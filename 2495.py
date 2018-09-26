lst = []
for i in range(3):
    lst.append(input())

result = []
for k in lst:
    cnt = 1
    temp = 0
    arr = list(k)
    for s in range(len(arr)-1):
        if arr[s] == arr[s+1]:
            cnt +=1
        else:
            if temp < cnt:
                temp = cnt
            cnt = 1
    if temp < cnt:
        temp = cnt
    result.append(temp)
for i in range(3):
    print(result[i])