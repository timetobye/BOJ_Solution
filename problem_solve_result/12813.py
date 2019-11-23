n = input()
m = input()

length = len(n)

# A & B
for i in range(length):
    if n[i] == '1' and m[i] == '1':
        print('1', end='')
    else:
        print('0', end='')
print()

# A | B
for i in range(length):
    if n[i] == '1' or m[i] == '1':
        print('1', end='')
    else:
        print('0', end='')
print()

# A ^ B
for i in range(length):
    if n[i] != m[i]:
        print('1', end='')
    else:
        print('0', end='')

print()

# ~A
for i in range(length):
    if n[i] == '1':
        print('0', end='')
    else:
        print('1', end='')

print()

# ~B
for i in range(length):
    if m[i] == '1':
        print('0', end='')
    else:
        print('1', end='')