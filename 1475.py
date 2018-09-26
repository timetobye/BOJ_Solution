import math

n = input()
n = n.replace('9', '6')
t = ','.join(n).split(',')

asdf = {}
for x in t:
    if x not in asdf:
        asdf[x] = 1
    else:
        asdf[x] += 1

if '6' in asdf:
    if (asdf['6'] % 2) == 0:
        asdf['6'] = asdf['6'] / 2
    else:
        if asdf['6'] == 1:
            asdf['6'] = 1
        else:
            asdf['6'] = math.ceil(asdf['6'] / 2)

print(int(max(asdf.values())))