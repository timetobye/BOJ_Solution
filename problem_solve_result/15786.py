from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]
password = input()

while m > 0:
    searched_string = []
    string_list = list(stdin.readline().strip())

    for word in password:
        try:
            index_number = string_list.index(word)
            word = string_list[index_number]
            string_list = string_list[index_number+1:]
            searched_string.append(word)
        except:
            continue
    joined_word = ''.join(searched_string)
    if password == joined_word:
        print('true')
    else:
        print('false')
    m -= 1
