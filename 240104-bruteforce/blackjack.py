N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))
result = []
for idx in range(N):
  for idx2 in range(idx+1, N):
    for idx3 in range(idx2+1, N):
      if cards[idx] + cards[idx2] + cards[idx3] <= M:
        result.append(cards[idx] + cards[idx2] + cards[idx3])

result = sorted(list(set(result)))

for idx, num in enumerate(result):
  if num <= M:
    print(result[idx-1])
    break