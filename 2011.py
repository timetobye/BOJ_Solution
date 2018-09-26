n = input()
arr = [int(x) for x in list(n)] # 숫자 리스트로 전환
le = len(arr) # 길이
dp = [0 for x in range(le+1)]
dp[0] = 1
for i in range(1,le+1):
    if (1<= arr[i-1] ) and (arr[i-1]<=9): # arr은 i-1부터 시작한다.
        dp[i] = dp[i] + dp[i-1]
    if i == 1:
        continue
    value = (arr[i-2] * 10 + arr[i-1]) # 두 자리 수를 구하기 위한 작업 arr은 i-1부터 하니까 i-2, i-1
    if (10<= value) and (value <=26):
        dp[i] = dp[i] + dp[i-2]
print(dp[le] % 1000000) # 마지막 값을 구한다.