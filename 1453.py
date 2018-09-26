n = int(input())
m = list(map(str, input().split()))
lst = []
cnt = 0
for i in range(n):
    if m[i] not in lst:
        lst.append(m[i])
    else:
        cnt +=1
print(cnt)