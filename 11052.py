n = int(input())
value = [int(x) for x in input().split()]
value.insert(0,0) # 계산 편의를 위해 가격 앞에 0을 넣었음
dp = [0 for x in range(n+1)]
for i in range(1, n+1): # 몇 개를 팔 것인가?
    for j in range(1,i+1): # 어떻게 팔 것인가? 나눠서 팔 것인가, 한 꺼번에 다 팔 거인가, 분할 계산
        dp[i] = max(dp[i], dp[i-j] + value[j])
print(dp[n])

'''

http://jaemin8852.tistory.com/168
이분의 글을 참고하여 풀이를 하였습니다.

'''