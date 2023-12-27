n = int(input())
init = 2
for idx in range(n):
  init += init - 1
print(init**2)
