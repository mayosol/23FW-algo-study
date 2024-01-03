# 3
# 124
# 25
# 194

# 25
# 10
# 5
# 1

coins = [25, 10, 5, 1]

for _ in range(int(input())):
  change = int(input())
  
  result = []
  
  for coin in coins:
    quo = change // coin
    remain = change % coin
    result.append(change // coin)
    change = remain

  print(*result)