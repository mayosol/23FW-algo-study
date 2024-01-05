N = int(input())
num, cnt = 665, 0

while cnt != N:
  num += 1
  if '666' in str(num):
    cnt += 1

print(num)