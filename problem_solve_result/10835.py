from sys import stdin

n = int(stdin.readline())

left_card_dummy = [int(x) for x in stdin.readline().split()]
right_card_dummy = [int(x) for x in stdin.readline().split()]

# reversed card dummy

left_card_dummy.reverse()
right_card_dummy.reverse()

# print(left_card_dummy, right_card_dummy)


dp = [0 for i in range(n + 1)]

count = 0
while True:
    if len(left_card_dummy) == 0 or len(right_card_dummy) == 0:
        break

    if left_card_dummy[0] <= right_card_dummy[0]:
        max_left_card_value = max(left_card_dummy)
        max_right_card_value = max(right_card_dummy)
        if (max_left_card_value == left_card_dummy[0]) and (max_right_card_value == right_card_dummy[0]):
            left_card_dummy = left_card_dummy[1:]
            right_card_dummy = right_card_dummy[1:]
            continue

        left_card_dummy = left_card_dummy[1:]
        continue

    if left_card_dummy[0] > right_card_dummy[0]:
        dp += right_card_dummy[0]
        right_card_dummy = right_card_dummy[1:]
        continue

print(dp)
