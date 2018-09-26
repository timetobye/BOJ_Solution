burger = []
drink = []
for x in range(3):
    burger.append(int(input()))
for y in range(2):
    drink.append(int(input()))

value = 5000
for i in burger:
    for j in drink:
        menu = i + j - 50
        if menu < value:
            value = menu
print(value)