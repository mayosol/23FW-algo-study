word = list(input().lower())
word.sort()

count_dict = {}
prev = ''

for char in word:
  if(char != prev):
    count_dict[char] = 1
  else:
    count_dict[char] += 1
  
  prev = char

result = ('', 0, False)

for char, count in count_dict.items():
  _, max_count, _ = result
  
  if count > max_count:
    result = (char, count, False)
  elif count == max_count:
    result = (char, count, True)

print('?' if result[2] else result[0].capitalize())