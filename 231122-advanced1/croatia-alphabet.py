def croatia_alphabet(word):
  croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
  for croa in croatia:
    word = word.replace(croa, '*')
  print(len(word))
        
croatia_alphabet('ljes=njak')