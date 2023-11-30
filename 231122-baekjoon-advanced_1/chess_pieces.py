# in order of (K, Q, R, B, K, P)
pieces = input()
pieces = [int(p) for p in pieces.strip().split(' ')]

# in order of (K, Q, R, B, K, P)
correct_pieces = [1, 1, 2, 2, 2, 8]

result = ""

for cp, p in zip(correct_pieces, pieces):
  result += f'{cp - p} '

print(result.strip())