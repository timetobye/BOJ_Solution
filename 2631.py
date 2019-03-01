"""
문제 접근이 어려울 수 있다.
아무리 봐도 알쏭달쏭 해서 찾아보니 LIS 문제였다.
LIS를 찾고 그것에 해당되지 않는 값만 옮기면 최소로 아이들을 옮길 수 있다.
예제에서는 3,5,6이 최종적으로 배치되어야 할 1,2,3,4,5,6,7의 부분집합 배열로 구성되어 있으므로
LIS를 구한 다음 전체 길이에서 LIS를 빼면 된다.
"""

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(len(arr) - max(dp))

