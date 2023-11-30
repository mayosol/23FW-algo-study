word = input()
word = list(word)

search_bound = len(word)//2

flag = 1

for idx in range(search_bound):
  idx_sym = len(word) - 1 - idx
  if word[idx] != word[idx_sym]:
    flag = 0

print(flag)