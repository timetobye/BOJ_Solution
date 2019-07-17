n, k = map(int, input().split())
arr = []
for x in range(n):
    arr.append(int(input()))
dp = [0]

for i in range(1,k+1):
    temp = []
    for j in arr:
        if j>i:
            continue
        if dp[i-j] == -1:
            continue
        temp.append(dp[i-j]+1)
    if not temp:
        dp.append(-1)
    else:
        res = min(temp)
        dp.append(res)

print(dp[k])