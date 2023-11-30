def word_study(word):
  from collections import Counter
  count_char = Counter(word.upper()).most_common()
  print(count_char)
  if len(count_char) > 1 and count_char[0][1] == count_char[1][1]:
    print('?')
  else:
    print(count_char[0][0])
  
word_study('zZZZzzsadfasdzz')

# Counter 안쓰고 만들어보기