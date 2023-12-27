X = int(input())

last, layer = 0, 0
while last < X:
  layer += 1
  last += layer

steps = last - X

if (layer) % 2 == 0:
  num = 1 + steps
  denom = layer - steps
else:
  num = layer - steps
  denom = 1 + steps
    
print(f'{denom}/{num}')
