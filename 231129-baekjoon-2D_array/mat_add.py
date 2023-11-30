n_row = int(input().split()[0])

mats = []
for _ in range(n_row * 2):
  mats.append( input().split() )

for idx in range(n_row):
  mat_a = mats[idx]
  mat_b = mats[idx + n_row]
  print(*[ int(a) + int(b) for a, b in zip(mat_a, mat_b)])