lst = []
data = list(input())
for x in data:
    try:
        if type(int(x)) == int:
            lst.append(str(x))
    except:
        if x == ' ':
            lst.append(x)
        else:
            t = ord(x)
            if t>=65 and t<=90:
                kkk = t + 13
                if kkk > 90:
                    kkk = kkk -26
                    lst.append(chr(kkk))
                else:
                    lst.append(chr(kkk))
            elif t>=97 and t<=122:
                kkk = t + 13
                if kkk>122:
                    kkk = kkk -26
                    lst.append(chr(kkk))
                else:
                    lst.append(chr(kkk))
result = ''.join(lst)
print(result)