"""
아.......뭐 문제가 이러냐..

문제 풀이 방법
1. 우선 1부터 12까지 손수 다 구했다.(0 to n을 12번 했음)
2. 구한걸 살펴보니 제곱수를 기준으로 규칙이 형성되는 부분이 있다.
  - input으로 주어지는 값을 모두 다 0을 기준으로 새롭게 치환하였다.
  - start_y = start_y - start_x, start_x = start_x - start_x
3. 주어진 범위를 포함 할 수 있는 N^2 과 그에 따른 (N-1)^2을 찾은 후에 각 경계에서 형성되는 것을 정리 하였다.
  - sqrt_value_large, sqrt_value_small
  - math.sqrt와 ceil(올림) 기능을 사용
4. 그리고 다시 check_large_small, check_large_value로 제곱수를 찾았다.
5. 구간 사이즈에 대한 값을 정리해서 count_value로 답을 구하였다.
6. 솔직히 좋은 코드는 아닌 것 같다.
"""


import math

tc = int(input())

for i in range(tc):
    start_x, start_y = [int(x) for x in input().split()]

    start_y = start_y - start_x
    start_x = start_x - start_x

    sqrt_value_large = math.ceil(math.sqrt(start_y))
    sqrt_value_small = sqrt_value_large - 1

    check_large_small = sqrt_value_small ** 2
    check_large_value = sqrt_value_large ** 2

    if (check_large_small - sqrt_value_small) < start_y <= check_large_small:
        count_value = 2 * sqrt_value_small - 1
    elif check_large_small < start_y <= (check_large_value - sqrt_value_large):
        count_value = 2 * sqrt_value_small
    elif (check_large_value - sqrt_value_large) < start_y <= check_large_value:
        count_value = 2 * sqrt_value_large - 1
    else:
        count_value = 2 * sqrt_value_large

    print(count_value)




