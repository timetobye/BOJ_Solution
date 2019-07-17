from collections import deque


def get_number(n, m, importance_list):
    cnt = 0

    check = [x for x in range(1, n+1)]
    check_q = deque(check)
    value = check[m]

    importance_q = deque(importance_list)

    while True:
        max_im_q = max(importance_q)
        if max_im_q == importance_q[0]:
            cnt += 1
            importance_q.popleft()
            ret = check_q.popleft()
            if value == ret:

                return cnt

            continue
        check_q.rotate(-1)
        importance_q.rotate(-1)


def main():
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        importance_list = [int(x) for x in input().split()]
        result = get_number(n, m, importance_list)
        print(result)


if __name__ == "__main__":
    main()
