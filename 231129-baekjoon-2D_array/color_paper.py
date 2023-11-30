white = [0] * (100 ** 2)

for _ in range(int(input())):
  bl_x, bl_y = map(int, input().split(' '))
  
  for y in range(10):
    for x in range(10):
      idx = (y + bl_y) * 100 + ( x + bl_x )
      if white[idx] != 1:
        white[idx] = 1

print(sum(white))