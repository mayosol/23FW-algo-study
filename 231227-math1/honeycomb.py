N = int(input()) - 1
layer, last = 1, 0

while last < N: 
  last += layer * 6
  layer += 1

print(layer)
