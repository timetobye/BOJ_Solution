# import re
#
# string = input()
# bomb = input()
#
# regex = re.compile(bomb)
# checker = None
#
# while True:
#     string = re.sub(regex, "", string)
#
#     if len(string) == 0:
#         print("FRULA")
#         break
#
#     if checker == string:
#         print(string)
#         break
#
#     checker = string


string_all = input()
bomb_string = input()
bs_len = len(bomb_string)
bomb_string_last = str(bomb_string[-1])

result_string_stack = ""

j = 0
for i, value in enumerate(string_all):
    result_string_stack += string_all[i]

    if value == bomb_string_last:

        if result_string_stack[(j-bs_len+1):] == bomb_string:
            j -= bs_len
            result_string_stack = result_string_stack[:j+1]

    j += 1

res = len(result_string_stack)

if res == 0:
    print("FRULA")
else:
    print(result_string_stack)


