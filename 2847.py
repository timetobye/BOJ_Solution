n = int(input())
lst = []
for x in range(n):
    lst.append(int(input()))

cnt = 0
for i in range(n-1,-1,-1):
    if i == 0:
        while lst[0] >= lst[1]:   #범위를 벗어날 수 있어서
            lst[0] -= 1
            cnt +=1
    else:
        while lst[i-1] >= lst[i]: #가장 먼 곳부터 정렬
            lst[i-1] -= 1
            cnt +=1
print(cnt)