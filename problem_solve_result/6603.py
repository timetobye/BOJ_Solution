from itertools import combinations

while True:
    lotto = [int(x) for x in input().split()]
    selecting_number = lotto[0]
    if selecting_number == 0:
        break

    combine_number_list = lotto[1:]

    for lotto_list in combinations(combine_number_list, 6):
        print(*lotto_list)

    print()