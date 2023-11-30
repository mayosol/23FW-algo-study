words = [
  'ljes=njak', #6
  'ddz=z=', # 3
  'nljj', # 3
  'c=c=', # 2
  'dz=ak', # 3
  'c=kc-zdz=d-jljnnjs=szz=' # 14 'c= k c- z dz= d- j lj n nj s= s z z='
]

# croatians = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

def search(idx, char_ls):
  curr = char_ls[idx]
  result = char_ls
  
  if curr == '=' or curr == '-' or ( curr == 'j' and ( char_ls[idx-1] == 'l' or char_ls[idx-1] == 'n') ):
    prev = char_ls[idx-1]
    joint = prev + curr
    result = char_ls[:idx-1] + [joint] + char_ls[idx+1:]
    
    if joint == 'z=' and (pprev := char_ls[idx-2]) == 'd':
      joint = pprev + joint
      result = char_ls[:idx-2] + [joint] + char_ls[idx+1:]
  
  return result

#### submit
word = list(input())
index = 0

while True:
  if len(word) - 1 < index:
    break
  
  word = search(index, word)
  if(index < len(word)):
    word = search(index, word)
  
  index += 1

print(len(word))


##### single case
# word = list(words[2])
# index = 0

# while True:
#   if len(word) - 1 < index:
#     break
  
#   word = search(index, word)
#   if(index < len(word)):
#     word = search(index, word)
  
#   index += 1

# print(len(word))


# #### multi case
# for word in words:
#   word = list(word)
#   index = 0

#   while True:
#     if len(word) - 1 < index:
#       break
    
#     word = search(index, word)
#     if(index < len(word)):
#       word = search(index, word)
    
#     index += 1

#   print(len(word))