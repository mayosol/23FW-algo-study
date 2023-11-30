def palindrome(word):
  mid = len(word) // 2
  result = 1
  for idx in range(mid):
    if word[idx] != word[len(word) - 1 - idx]:
      result = 0
      break
  return result

palindrome('baekjoon')
