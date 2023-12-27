coins = [25, 10, 5, 1]
for case in range(int(input())):
  result = []
  change = int(input())
  for coin in coins:
    result.append(change//coin)
    change %= coin
  print(*result)
  