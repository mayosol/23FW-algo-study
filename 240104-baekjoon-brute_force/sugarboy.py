# 3 <= n <= 5000

n = int(input())

res = -1

fives = n // 5
r = n % 5

while True:
  if r > n:
    break
  
  if r == 0:
    res = fives
    break
    
  if r % 3 == 0 and r != 0:
    res = fives + (r // 3)
    break
  
  fives -= 1
  r += 5

print(res)