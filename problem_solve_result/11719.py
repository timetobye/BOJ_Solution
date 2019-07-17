h = []
while True:
    try:
        s = input()
        h.append(s)
    except:
        break
for i in range(len(h)):
    print(h[i])