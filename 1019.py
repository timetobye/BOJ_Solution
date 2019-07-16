n = int(input())

book_all_page_number = list(range(1, n + 1))
number_count_dict = {'0': 0}

for value in book_all_page_number:
    value_str = str(value)

    for number in value_str:
        if number not in number_count_dict:
            number_count_dict[number] = 1
        else:
            number_count_dict[number] += 1

res = number_count_dict.values()
print(*res)
