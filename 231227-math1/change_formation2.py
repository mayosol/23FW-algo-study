b_form = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())
result= ''

while N:
  q, r = divmod(N, B)
  result += b_form[r]
  N //= B

print(result[::-1])
