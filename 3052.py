result = set()
for i in range(10):
    n = int(input())
    num = str(int(n%42))
    result.add(num)
print(len(result))