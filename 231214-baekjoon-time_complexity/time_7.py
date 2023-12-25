a1, a0 = [int(st) for st in input().split(' ')]

c = int(input())

n0 = int(input())

f_ = lambda x: (a1 - c) * x + a0

result = 0

if a1 <= c:
  if a1 == c and a0 <= 0:
    result = 1
  elif a1 < c:
    if f_(n0) <= 0:
      result = 1

print(result)