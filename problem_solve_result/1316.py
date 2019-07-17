n = int(input())
temp = 0
for _ in range(n):
    cnt = 0
    asdf = {}
    a = list(input())
    for i in range(len(a)):
        t = a[i]
        if t not in asdf:
            asdf[t] = str(a.index(t))
            a[i] = " "
        else:
            asdf[t] = asdf[t] + "," + str(a.index(t))
            a[i] = " "

    for z in asdf:
        k = list(map(int, asdf[z].split(',')))
        if len(k) ==1:
            pass
        else:
            for p in range(len(k)-1):
                f = k[p+1] - k[p]
                if f != 1:
                    cnt += 1
    if cnt == 0:
        temp +=1
print(temp)

'''
- 어떤 문자열에 대해서 각 문자에 대한 인덱스 번호를 하나씩 뽑은 후에 그 번호들의 차이가 1이 아니면 
  그 문자는 그룹 단어가 아니다.
- 유니크한 문자수만큼 for문이 돌아야겠네
'''