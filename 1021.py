from collections import deque

n, m = map(int, input().split())
find_number_list = [int(x) for x in input().split()]

numbers = [int(x) for x in range(1, n+1)]
d = deque(numbers)

all_count = 0
for number in find_number_list:
    left_count = 0
    right_count = 0
    d_left = d.copy()
    d_right = d.copy()

    while True:
        if d_left[0] == number:
            d_left.popleft()
            break
        d_left.rotate(-1)
        left_count += 1

    while True:
        if d_right[0] == number:
            d_right.popleft()
            break
        d_right.rotate(1)
        right_count += 1

    if left_count <= right_count:
        all_count += left_count
        d = d_left
    else:
        all_count += right_count
        d = d_right

print(all_count)

"""
참고
https://godoftyping.wordpress.com/tag/%EC%96%91%EB%B0%A9%ED%96%A5-%ED%81%90/
http://simsimjae.tistory.com/3
http://simsimjae.tistory.com/4
"""





