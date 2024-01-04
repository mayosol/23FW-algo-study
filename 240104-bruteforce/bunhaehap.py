N = int(input())

for n in range(1, N):
  str_n = list(str(n))
  sum_n = n + sum(map(int, str_n))
  if sum_n == N:
    print(n)
    break
else:
  print(0)
  