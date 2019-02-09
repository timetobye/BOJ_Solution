"""
1. max_length를 구해서 각 list내에서 최대로 확인해야 할 길이를 구했다.

2. try / except으로 최대 길이보다 작은 구간에서는 pass하도록 하였다.

"""


arr = []
max_length = 0
for j in range(5):
    temp = list(input())
    if max_length < len(temp):
        max_length = len(temp)
    arr.append(temp)

for i in range(max_length):
    for j in range(5):
        try:
            value = arr[j][i]
            if value != " ":
                print(value, end="")
        except:
            pass
