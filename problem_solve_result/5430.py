"""
꼬여서 너무 힘들게 풀었다. 향후 삽질을 반복하지 않기 위해 처음에 쉽게 생각했던 코드도 남겨둔다.
- 핵심은 문자열로 리스트가 들어오고 파싱을 잘 한 다음에....-> deque 에 넣은 후 빈 문자열에 대해서는 별도 처리 <- 이게 핵심
- 그리고 reverse 를 할 경우 시간 초과가 걸리는 것 같으니 flag 로 대체하고 pop, popleft 로 처리를 하면 된다.
- 참고 : https://hongcoding.tistory.com/44
"""

from collections import deque
from sys import stdin


def main():
    test_case = int(stdin.readline())

    for i in range(test_case):
        # function string like RDD, RR
        function_strings = stdin.readline().strip('\n')

        # arr string count
        n = int(stdin.readline())

        # parsing : arr string -> arr
        arr = stdin.readline().strip()[1:-1].split(",")
        q = deque(arr)

        if n == 0:
            q = deque([])

        reversed_status = 0

        for function_string in function_strings:
            if function_string == "R":
                if reversed_status == 0:
                    reversed_status = 1
                else:
                    reversed_status = 0
            else:
                if len(q) == 0:
                    print("error")
                    break
                if reversed_status == 1:
                    q.pop()
                else:
                    q.popleft()
        else:
            if reversed_status == 1:
                q.reverse()
            print("[" + ",".join(q) + "]")


if __name__ == "__main__":
    main()

"""
1
RDRDRDRDRDRDD
6
[1,2,3,4,5,6]

1
RDD
4
[1,2,3,4]

1
DD
1
[42]

1
RRD
6
[1,1,2,3,5,8]

1
D
0
[]
"""

"""
def main():
    test_case = int(stdin.readline())

    for i in range(test_case):
        # function string like RDD, RR
        function_strings = stdin.readline().strip('\n')
        function_strings = function_strings.replace("RR", "")

        # arr string count
        n = int(stdin.readline())

        # parsing : arr string -> arr
        arr = stdin.readline().strip()[1:-1].split(",")
        if n == 0:
            arr = []

        reversed_status = 0

        while len(function_strings) >= 2:
            # print("----")
            # print(arr, function_strings)
            if function_strings[0:2] == "DD":
                if reversed_status == 0:
                    arr = arr[2:]
                else:
                    arr = arr[:-2]
            elif function_strings[0:2] == "RD":
                if reversed_status == 0:
                    arr.pop(-1)
                    reversed_status = 1
                else:
                    arr.pop(0)
                    reversed_status = 0
            function_strings = function_strings[2:]

        # print(function_strings, arr, reversed_status, len(arr))
        if reversed_status == 1:
            arr.reverse()

        if len(function_strings) == 0:
            if len(arr) > 0:
                print("["+",".join(arr)+"]")
            else:
                print("error")
            continue
        elif len(arr) == 0 and function_strings == "D":
            print("error")
        elif function_strings == "R":
            arr.reverse()
            print("["+",".join(arr)+"]")
        elif function_strings == "D":
            arr.pop(0)
            print("[" + ",".join(arr) + "]")
        else:
            print("["+",".join(arr)+"]")


if __name__ == "__main__":
    main()
"""


"""


아...모르겠다...일단 다시 생각해보자.



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
"""