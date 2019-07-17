n = input()
lst = list(input().split())

cnt = 0
for i in lst:
    if n == i:
        cnt +=1
print(cnt)