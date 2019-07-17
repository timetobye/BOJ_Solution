row, column = input().split()
row_lst = list(row)
column_lst = list(column)
cnt = 0
for word in row_lst:
    try:
        idx = column_lst.index(word)
        break
    except:
        cnt +=1
for x in range(len(column_lst)):
    if x == idx:
        print(row)
        continue
    for y in range(len(row_lst)):
        if y == cnt:
            print(column[x], end="")
        else:
            print('.', end="")
    print()