n = int(input())
asc = [int(num) for num in input().split()]

dp_a = [1 for x in range(n)]
dp_d = [1 for x in range(n)]
for i in range(n):
    for j in range(i):
        if (dp_a[i] < (dp_a[j] + 1)) and (asc[j]<asc[i]):
            dp_a[i] = dp_a[j] + 1

des = [int(num) for num in asc[::-1]]
for i in range(n):
    for j in range(i):
        if (dp_d[i] < (dp_d[j] + 1)) and (des[j]<des[i]):
            dp_d[i] = dp_d[j] + 1
dp_d.reverse()  # 배열을 원래대로 돌려줘서 두 배열 합 중 가장 큰 값 - 1

value = 0
for i in range(n):
    t = (dp_a[i] + dp_d[i] - 1)
    if value < t:
        value = t
print(value)