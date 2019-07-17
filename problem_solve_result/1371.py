lst = []

while True:
    try:
        lst += list(input())
    except:
        break

arr = {}

for x in lst:
    if x not in arr:
        arr[x] = 1
    else:
        arr[x] += 1

if ' ' in arr:
    del arr[' ']

result = []
for y in arr:
    if arr[y]==(max(arr.values())):
        result.append(y)
result.sort()

for k in result:
    print(k, end="")