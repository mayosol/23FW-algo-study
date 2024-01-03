target = int(input())

index = 1
count = 1

while target > 1:
  count += index * 6
  
  index += 1
  
  if count >= target:
    break

print(index)