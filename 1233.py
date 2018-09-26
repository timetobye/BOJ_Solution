s1, s2 , s3 = map(int, input().split())

res = {}
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            temp = i + j + k
            if temp not in res:
                res[temp] = 1
            else:
                res[temp] += 1

max_value = max(res.values())

st = set()
for x in res:
    if res[x] == max_value:
        st.add(x)
print(min(st))