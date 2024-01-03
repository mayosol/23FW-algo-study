# row: numerator
# col: denominator

# pattern 
# 0: 1/1
# 1: 1/2
# 2: 2/1
# 3: 3/1

# 4: 2/2
# 5: 2/3
# 6: 3/2
# 7: 4/2

# set/set => set/set+1 => set+1/set => set+2/set
import math

summ = lambda x: int((x+1)*x/2)
reverse_sum = lambda x: math.ceil((-1 + math.sqrt(1 + 8*x)) / 2)

num = int(input())

n = reverse_sum(num)
is_even = n % 2 == 0

denom, numer = (n, 1) if is_even else (1, n)

if num > 1:
  num_iter = num - summ(n-1) - 1

  numer += num_iter * ( is_even + ( is_even - 1 ) )
  denom += num_iter * ( (not is_even) + ( (not is_even) - 1) )

print(f'{numer}/{denom}')