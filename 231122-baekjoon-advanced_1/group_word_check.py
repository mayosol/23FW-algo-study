num_word = int(input())

words = []
for _ in range(num_word):
  words.append(input())

for word in words:
  prev_char = ''
  count_dict = {}
  
  for char in word:
    if prev_char != char:
      if count_dict.get(char, 0) > 0:
        num_word -= 1
        break
      else:
        count_dict[char] = 1
    else:
      count_dict[char] += 1
    
    prev_char = char

print(num_word)