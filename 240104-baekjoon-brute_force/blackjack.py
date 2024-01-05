n, m = map(int, input().split())
cards = list(map(int, input().split()))

cur_max = 0

for idx, first in enumerate(cards):
  
  if first > m:
    continue
  
  for jdx, second in enumerate(cards[idx+1:]):
    
    if first + second > m:
      continue
    
    for third in cards[idx+jdx+2:]:
      hand = first + second + third
      
      if hand <= m and hand > cur_max:
        cur_max = hand


print(cur_max)