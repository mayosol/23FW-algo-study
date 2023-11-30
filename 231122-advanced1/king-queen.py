def chess(num_pieces):
  complete = [1, 1, 2, 2, 2, 8]
  num_pieces = num_pieces.split(' ')
  need = [complete[idx] - int(num_pieces[idx]) for idx in range(len(complete))]

  print(*need)
  
x = chess('10 10 10 10 10 10')