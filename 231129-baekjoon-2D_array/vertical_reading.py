vert = []

for _ in range(5):
  row = input()
  
  for char_idx, char in enumerate(row):
    if char_idx <= len(vert) - 1:
      vert[char_idx].append(char)
    else:
      vert.append([char])

print( ''.join( [ ''.join(line)  for line in vert ] ) )