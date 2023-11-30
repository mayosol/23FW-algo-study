matrix = []

for i in range(9):
  matrix.extend(map(int, input().split()))
  
max_idx = matrix.index(max(matrix))

print(max(matrix))
print((max_idx//9) + 1, (max_idx % 9) + 1)