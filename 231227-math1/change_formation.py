b_form = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, b = input().split()
N, b = reversed(list(N)), int(b)
result = 0

for idx, n in enumerate(N):
    result += (b_form.index(n)) * (b ** idx)
  
print(result)