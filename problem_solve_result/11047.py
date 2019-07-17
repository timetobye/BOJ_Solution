n, k = [int(x) for x in input().split()]

coins = []
for i in range(n):
    coins.append(int(input()))

coins = sorted(coins, reverse=True)

coin_count = 0

for coin in coins:
    value = k // coin
    coin_count += value

    if value > 0:
        k = (k - coin * value)

print(coin_count)