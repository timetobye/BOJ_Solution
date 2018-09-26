n = list(map(int, input().split(":")))
m = list(map(int, input().split(":")))

now = n[0] * 60 ** 2 + n[1] * 60 + n[2]
end = m[0] * 60 ** 2 + m[1] * 60 + m[2]

if now >= end:
    end += 24 * 60 ** 2

result = end - now

h = result // 3600
m = (result - h * 3600) // 60
s = result - h * 3600 - m * 60

if len(str(h)) == 1:
    h = "0" + str(h)
if len(str(m)) == 1:
    m = "0" + str(m)
if len(str(s)) == 1:
    s = "0" + str(s)

lst = [str(h), str(m), str(s)]

t = ':'.join(lst)

print(t)