k, n = list(map(int, input().split()))
cables = [ int(input()) for _ in range(k) ]

mn = 1
mx = max(cables)
center = 0

while mn <= mx:
  center = (mn + mx) // 2
  number = sum( map(lambda cab: cab//center, cables) )
  
  if number < n:
    mx = center - 1
  
  else:
    if sum( map(lambda cab: cab//(center+1), cables) ) < n:
      break
    mn = center + 1

print(center)