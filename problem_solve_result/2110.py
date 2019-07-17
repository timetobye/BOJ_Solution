# 간격을 구해야 하는 문제이다.
# 설정된 간격을 만족할 때 그 개수가 요구하는 갯수보다 같거나 크다면 값으로 추론할 수 있다.

n,target = map(int, input().split())
arr = []
for v in range(n):
    arr.append(int(input()))
arr.sort()
left = 1
right = arr[n-1] - arr[0]  # 최대 거리(가능)
ans = 0

#거리에 대해 접근해서 거리별로 설치가 가능한지를 판별하는 것
while left <= right:
    mid=(left+right)//2
    cnt=1   #현재 하나는 박혀 있다. mid가 설정 되어있으니까
    start = arr[0]

    for x in range(n):
        if (arr[x] - start) >= mid:
            cnt +=1
            start = arr[x]
    if cnt >= target:
        ans = mid
        left = mid +1
    else:
        right = mid -1
print(ans)