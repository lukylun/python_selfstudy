N = int(input())
coins = [500, 100, 50, 10, 5, 1]

changes = 1000 - N
ans = 0
for coin in coins:
    ans += (changes // coin)
    changes %= coin

print(ans)