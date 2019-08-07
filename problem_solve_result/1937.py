"""
1. dfs + dp
2. 모든 지점에서 완전 탐색을 하기 보다는 기록이 있는 부분을 재활용해서 시간초과와 메모리초과를 돌파
3. dfs로 갈 수 있는 최대 길이가 최대 일수
4. python에서 재귀를 쓸 때는 setrecursionlimit를 사용하면 런타임에러를 탈출 할 수 있다.
5. dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)
- 갈 수 있는 지점까지 간 다음 이전 단계와 비교해서 값을 구하는 방식으로 접근

참고한 선인의 지혜
- https://2youngjae.tistory.com/145
- https://stackoverflow.com/questions/40701961/finding-the-max-value-in-a-two-dimensional-array
"""

import sys
sys.setrecursionlimit(10000000)

n = int(input())

arrays = []
for i in range(n):
    array = [int(x) for x in input().split()]
    arrays.append(array)

dp = [[0 for i in range(n)] for j in range(n)]


# dfs

def dfs(y, x):
    if dp[y][x] == 0:
        dp[y][x] = 1
        vectors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

        for ny, nx in vectors:
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if arrays[ny][nx] > arrays[y][x]:
                if dp[ny][nx] == 0:
                    dfs(ny, nx)

                dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)


for j in range(n):
    for i in range(n):
        dfs(j, i)


max_value = max(map(max, dp))
print(max_value)
