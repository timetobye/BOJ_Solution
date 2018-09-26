n = int(input())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr.sort()
lst = brr.copy()
lst.sort(reverse = True)

krr = []
for i in range(n):
    krr.append(arr[i] * lst[i])

print(sum(krr))