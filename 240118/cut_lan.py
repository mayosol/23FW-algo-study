k, n = map(int, input().split())
lan_lines = [int(input()) for _ in range(k)]
min, max = 1, max(lan_lines)

while min <= max:
  length = (min + max) // 2
  cut_lan = sum([lan_line // length for lan_line in lan_lines])
  if cut_lan >= n:
    min = length + 1
  else:
    max = length - 1
  
print(max)