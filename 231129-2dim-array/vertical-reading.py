result = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
for i in range(5):
  row = input()
  for idx, char in enumerate(row):
    result[idx] += char
    
print(''.join(result))