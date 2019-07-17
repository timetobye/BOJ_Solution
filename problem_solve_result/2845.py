n, m = map(int, input().split())

square = n * m

news = list(map(int, input().split()))

result = list(map(lambda x : x-square, news))

for x in result:
    print(x, end=" ")   