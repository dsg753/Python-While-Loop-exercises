change = float(input())
change_in_cents = int(round(change * 100))

coins = [200, 100, 50, 20, 10, 5, 2, 1]

coin_count = 0

for coin in coins:
    while change_in_cents >= coin:
        change_in_cents -= coin
        coin_count += 1

print(coin_count)
