from itertools import combinations
card_cnt, card_max = map(int, input().split())
card = list(map(int, input().split()))
max_value = 0
for v in combinations(card, 3):
    if sum(v) > card_max:
        continue
    if sum(v) > max_value:
        max_value = sum(v)
print(max_value)