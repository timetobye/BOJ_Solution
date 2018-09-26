lst = ['2'*3, '3'*3, '4'*3, '5'*3, '6'*3, '7'*4, '8'*3, '9'*4]
new = []; alpha = []
for i in range(len(lst)):
    new += ','.join(lst[i]).split(',')

for i in range(97,123):
    alpha.append(chr(i))

asdf = {}
cnt = 0
for j in alpha:
    asdf[j] = new[cnt]
    cnt +=1

n = input().lower()

data = 0

for k in range(len(n)):
    if n[k] in asdf:
        data += int(asdf[n[k]])
    else:
        pass
print(data + len(n))