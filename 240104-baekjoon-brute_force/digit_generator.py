n = int(input())

min_exp = 6

for exp in range(6):
  if 10**exp <= n < 10**(exp+1):
    min_exp = exp
    break

res = 0

if min_exp > 0:
  for i in range(9 * (min_exp + 1), 0, -1):
    num = n - i
    
    if num <= 0:
      continue
    
    if num + sum(map(int, str(num))) == n:
      res = num
      break
else:
  if n % 2 == 0:
    res = n // 2

print(res)