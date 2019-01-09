def get_seventeen_prize(a):
    prize = [500, 300, 200, 50, 30, 10]
    if (a == 0) or (a > 21):
        return 0
    if a == 1:
        return prize[0]
    i = 2
    while True:
        formula = int((i ** 2 - i + 2) / 2)
        check_list = []
        for j in range(formula, formula + i):
            check_list.append(j)
        if a in check_list:
            return prize[i - 1]
        else:
            i += 1


def get_eighteen_prize(b):
    prize_max = 512
    i = 1
    if (b == 0) or (b > 31):
        return 0
    else:
        while True:
            rank = []
            for j in range(2 ** (i - 1), 2 ** (i)):
                rank.append(j)
            if b in rank:
                return prize_max // (2 ** (i - 1))
            else:
                i += 1


def main():
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        sum_result = get_seventeen_prize(a) + get_eighteen_prize(b)
        print(sum_result * 10000)


if __name__ == "__main__":
    main()