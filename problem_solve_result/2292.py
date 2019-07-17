n = int(input())
k = 0
x = 2
while True:
    y = x + 6 * (k+1)
    if n == 1:
        print(1)
        break
    elif n>= x and n< y:
        print(k+2)
        break
    else:
        k += 1
        x = y