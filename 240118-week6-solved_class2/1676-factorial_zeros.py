n = int(input())

fact = 1

for i in range(2, n+1):
  fact *= i
  
fact = str(fact)

res = 0

for c in reversed(fact):
  if c == '0':
    res += 1
  else: 
    break

print(res)