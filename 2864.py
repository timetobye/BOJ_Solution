n, m = map(str, input().split())

min_n, min_m = map(int, [n.replace("6","5"),m.replace("6","5")])
max_n, max_m = map(int, [n.replace("5","6"),m.replace("5","6")])

print(min_n + min_m, max_n + max_m)