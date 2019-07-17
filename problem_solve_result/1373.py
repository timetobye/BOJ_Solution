arr = list(str(input()))[::-1]
res = []
value = 0
for i in range(len(arr)//3 +1):
    key = arr[3*i:3*(i+1)]
    for j in range(len(key)):
        value += (int(key[j]) * 2**j) # 최대 3개씩 끊어서 처리
    res.append(str(value))
    value = 0
res = res[::-1]
ans = ''.join(res)
cnt = 0
if len(ans) == 1: # 0 한 개만 넣을 떄를 대비하기 위함
    pass
else:
    for i in range(len(ans)): # 최대 00xxx 을 거르기 위함
        if ans[i] == '0':
            ans = ans[1:]
        else:
            break
        cnt +=1
        if cnt == 2:
            break
print(ans)

'''
## 반례
- 110010101101100101011011001010110
- 0
'''