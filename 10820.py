lower = [chr(x) for x in range(97,123)]
upper = list(map(lambda x : x.upper(), lower))
digit = ['0','1','2','3','4','5','6','7','8','9']
space = ' '
while True:
    try:
        n = input()
        a,b,c,d = 0,0,0,0
        n = list(n)
        for i in range(len(n)):
            if n[i] in lower:
                a +=1
            elif n[i] in upper:
                b +=1
            elif n[i] in digit:
                c +=1
            elif n[i] == space:
                d +=1
        print(a,b,c,d, sep = " ")
    except:
        break