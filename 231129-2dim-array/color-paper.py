big_paper = [[0 for X in range(100)] for Y in range(100)]

for c_paper in range(int(input())):
  x, y = map(int, input().split())
  for row in range(10):
    big_paper[x+row][y:y+10] = [1] * 10
      
print(sum(sum(row) for row in big_paper))