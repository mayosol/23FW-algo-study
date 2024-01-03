# 0~9 // 48 ~ 57
# A: 10 // 65
# Z: 35 // 90

def char2num(char):
  num = ord(char)
  
  if 48 <= num <= 57:
    num -= 48
  else:
    num -= 55
  
  return num

num, base = input().split(' ')

result = 0

for exp, digit in enumerate(reversed(num)):
  result += char2num(digit) * int(base) ** exp

print(result)
