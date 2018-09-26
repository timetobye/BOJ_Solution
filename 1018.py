m, n = map(int, input().split())

n_st = []
a = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
b = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
for i in range(m):
    n_st.append(list(input()))
res = []
for i in range(m - 7):
    p_st = n_st[i:i + 8]
    for p in range(n - 7):
        l_st = []
        ct_1 = 0;
        ct_2 = 0;
        for q in range(8):
            l_st.append(p_st[q][p:p + 8])

        f = [];
        g = []
        for _ in range(4):
            f.append(a)
            f.append(b)
            g.append(b)
            g.append(a)

        for t in range(8):
            for w in range(8):
                if l_st[t][w] != f[t][w]:
                    ct_1 += 1
                if l_st[t][w] != g[t][w]:
                    ct_2 += 1
        res.append(min(ct_1, ct_2))
print(min(res))