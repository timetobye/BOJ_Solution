lst = 'aeiou'
lst = list(lst)

while True:
    n = input()
    if n == "#":
        break
    n = list(n)
    cnt = 0
    for x in n:
        if x.lower() in lst:
            cnt +=1
    print(cnt)
    cnt = 0