N = int(input())
Ns = set(input().split())
M = int(input())
Ms = input().split()

for m in Ms:
  if m in Ns:
    print(1)
  else:
    print(0)
    