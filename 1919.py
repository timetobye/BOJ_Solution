n = list(input())
m = list(input())

fr = {}
for x in n:
    if x not in fr:
        fr[x] = 1
    else:
        fr[x] += 1
br = {}
for x in m:
    if x not in br:
        br[x] = 1
    else:
        br[x] += 1

t1 = set(fr.keys())
t2 = set(br.keys())
word = t1 & t2
cnt = 0
for y in word:
    cnt += abs(fr[y] - br[y])

t3 = t1 - t2
for x in t3:
    cnt += fr[x]
t4 = t2 - t1
for y in t4:
    cnt += br[y]

print(cnt)