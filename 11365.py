arr = []
while True:
    n = input()
    if n == 'END':
        break
    else:
        arr.append(n)
for i in range(len(arr)):
    print(arr[i][::-1])