def pro(n):
    result = n
    for i in range(len(str(n))):
        result += int(str(n)[i])
    return result


full = list(range(1, 10001))
arr = []
for i in range(1, 10001):
    arr.append(pro(i))

result = sorted(list(set(full) - set(arr)))
for i in result:
    print(i)