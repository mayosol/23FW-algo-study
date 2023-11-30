n, m = map(int, input().split())

matrixs = []
for i in range(n * 2):
  matrixs.append(list(map(int, input().split())))
  
for idx in range(n):
  result = [x + y for x, y in zip(matrixs[idx], matrixs[idx+n])]
  print(' '.join(str(num) for num in result))
  