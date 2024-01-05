n = int(input())

cnt = 1
curr = 666

while n > 1:
  curr += 1
  
  if '666' in str(curr):
    cnt += 1
      
    if cnt == n:
      break

print(curr)