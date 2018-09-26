case = list(input())
lst = []
idx = []
cnt = 0
i_cnt = 0
for x in case:
    if x == '(':
        idx.append(i_cnt)
    else:
        if (i_cnt - idx[-1]) == 1:
            idx.pop()
            cnt += len(idx)
        else:
            idx.pop()
            cnt += 1
    i_cnt +=1
print(cnt)