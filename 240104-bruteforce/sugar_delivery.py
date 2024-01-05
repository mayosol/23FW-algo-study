sugar = int(input())

for small in range(sugar // 3 + 1):
  sugar_left = sugar - small * 3
  if sugar_left % 5 == 0:
    print(small + sugar_left // 5)
    break
else:
  print(-1)
