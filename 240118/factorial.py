N = int(input())
fact = 1
for i in range(2, N + 1):
  fact *= i
  
zeros = 0
for num in str(fact)[::-1]:
  if num != '0':
    print(zeros)
    break
  else:
    zeros += 1
    
    
# 2번째
zeros2 = 0
while fact % 10 == 0:
  fact //= 10
  zeros2 += 1
