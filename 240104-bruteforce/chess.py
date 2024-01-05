X, Y = map(int, input().split(' '))
chess = []
for i in range(X):
  row = list(input())
  chess.append(row)

cnt_paint = []
w, b = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
white, black = [w, b, w, b, w, b, w, b], [b, w, b, w, b, w, b, w]

for row in range(X-7):
  for col in range(Y-7):
    new_chess = [chess_row[col:col+8] for chess_row in chess[row:row+8]]
    paint_white = sum([a != b for row1, row2 in zip(new_chess, white) for a, b in zip(row1, row2)])
    paint_black = sum([a != b for row1, row2 in zip(new_chess, black) for a, b in zip(row1, row2)])
    cnt_paint.append(paint_white)
    cnt_paint.append(paint_black)

print(min(cnt_paint))
    