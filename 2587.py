from statistics import median
lst = []
for i in range(5):
    n = int(input())
    lst.append(n)

avg = int(sum(lst) / len(lst))
md = median(lst)
print(avg)
print(md)