from collections import deque

n = int(input())

arr = [int(x) for x in range(1, 10)]
q = deque(arr)
dp = [0]

"""
basic_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_number = 9876543210
만들 수 있는 가짓 수 = 2**10 -1 = 1023개(모든 부분 집합 - 공집합)
1023개를 넘는 n이 들어오면 -1로 다 튕겨내면 된다.

temp 값의 마지막 값만을 계속 비교해야 하는 것을 놓쳤었다.
그래서 중간에 100, 200이 dp에 들어가 있었다.

"""
if n >= 1023:
    print(-1)
else:
    while q:
        temp = q.popleft()
        dp.append(temp)
        for i in range(0, 10):
            if int(str(temp)[-1]) > i:
                value = int(str(temp) + str(i))
                q.append(value)
        try:
            print(dp[n])
            break
        except:
            pass

