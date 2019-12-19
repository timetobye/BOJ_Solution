from collections import deque
from sys import stdin

"""
아...모르겠다...일단 다시 생각해보자.
"""


def reverse_order(string):
    if string == 'R':
        flag_number = 1
    else:
        flag_number = 0

    return flag_number


def remove_first_number(source_list, flag_value):
    if flag_value == 1:
        source_list.pop()
    else:
        source_list.popleft()

    return source_list


def call_order(flag_number, source_list):
    result = remove_first_number(source_list, flag_number)

    return result


test_case = int(stdin.readline())

for _ in range(test_case):
    order_list = list(stdin.readline().strip('\n'))
    n = int(stdin.readline())
    res = stdin.readline()[1:-2]

    if len(res) != 0:
        arr = [int(x) for x in res.split(',')]
    else:
        arr = ''

    deque_arr = deque(arr)
    # print(deque_arr)

    reverse_count = order_list.count('R')
    flag_value = 0

    for order in order_list:
        # print(order)
        if n == 0:
            print('error')
            break

        if len(deque_arr) == 0:
            print('error')
            break

        if order == 'R':
            if flag_value == 1:
                flag_value = 0
            else:
                flag_value = reverse_order(order)
            continue
        else:
            deque_arr = call_order(flag_value, deque_arr)

        if len(deque_arr) == 0:
            print('error')
            break

    if len(deque_arr) != 0:
        if flag_value % 2 == 0:
            print(list(deque_arr))
        else:
            print(list(reversed(deque_arr)))
