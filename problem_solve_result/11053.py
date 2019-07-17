n = int(input())
arr = list(map(int, input().split()))
dp = [1 for x in range(n)] # 모든 경우의 최소는 자기자신의 길이 1이다.
for i in range(n): # n 번만큼 돌거고..
    for j in range(i): # 자기 자신까지만 체크해주면 되니까
        if (j<i) and (arr[j]<arr[i]): # 문제의 조건을 구현
            result = dp[j] + 1 # 결과
            if result > dp[i]: # 이전 결과와 비교하여 크면 변경
                dp[i] = result
print(max(dp))