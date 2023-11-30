def group_word_checker(num_word, word):
  for num in range(num_word):
    for idx, char in enumerate(word):
      if char != word[idx + 1] and char in word[idx + 1:]:
        num_word -= 1
  return(num_word)
