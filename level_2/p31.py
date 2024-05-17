# find the number of ways that £2 can be made using
# any number of coins: 1p, 2p, 5p, 20p, 50p, 100p(£1) and 200p(£2)

def find_num_ways(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
    return ways[amount]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200

tot_ways = find_num_ways(amount, coins)
print(tot_ways)