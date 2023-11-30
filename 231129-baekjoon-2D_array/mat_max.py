max_val = (0, 1, 1)

for row_idx in range(9):
  for col_idx, char in enumerate(input().split()):
    if (val := int(char)) > max_val[0]:
      max_val = (val, row_idx+1, col_idx+1)

print(max_val[0])
print(*max_val[1:])