a, b = map(int, input().split())
c, d = map(int, input().split())

sum1 = a/c + b/d
sum2 = c/d + a/b
sum3 = c/a + d/b
sum4 = b/a + d/c

res = [sum1, sum2, sum3, sum4]
print(res.index(max(res)))