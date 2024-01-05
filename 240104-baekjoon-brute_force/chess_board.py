# starts with W
templ_w = [ 
  [87, 66, 87, 66, 87, 66, 87, 66],
  [66, 87, 66, 87, 66, 87, 66, 87]
]

templ_b = [ 
  [66, 87, 66, 87, 66, 87, 66, 87],
  [87, 66, 87, 66, 87, 66, 87, 66]
]

def arr_cmpr(src, tar):
  diff = 0
  
  for i in range(len(src)):
    if src[i] != tar[i]:
      diff += 1
  
  return diff

h, w = map(int, input().split())

board = []

for _ in range(h):
  # board.append(input())
  board.append( list( map(ord, input()) ) )

res = 2500

for h_off in range(h - 7):
  for w_off in range(w - 7):
    diff_w = sum( [ arr_cmpr(row[w_off: w_off + 8], templ_w[idx % 2]) for idx, row in enumerate(board[h_off: h_off + 8]) ] )
    diff_b = sum( [ arr_cmpr(row[w_off: w_off + 8], templ_b[idx % 2]) for idx, row in enumerate(board[h_off: h_off + 8]) ] )
    diff = min(diff_w, diff_b)
    if diff < res:
      res = diff

print(res)