# 0~9 // 48 ~ 57
# A: 10 // 65
# Z: 35 // 90

def num2char(num):
  if 10 <= num <= 35:
    return chr(num + 55)
  else:
    return f'{num}'

num, base = list(map(lambda x: int(x), input().split(' ')))

result = ''

while True:
  remain = num % base
  quo = num // base
  
  result = num2char(remain) + result
  
  if(quo == 0):
    break
  
  num = quo

print(result)
