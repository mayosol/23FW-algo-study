n = int(input())
seq = [ int(input()) for _ in range(n) ]

cnt = 0
stack = []
command = []

for num in seq:
  last_idx = len(stack) - 1
  
  if len(stack) > 0 and stack[len(stack) - 1] == num:
    stack.pop()
    command.append('-')
  
  elif num > cnt:
    for i in range(1, (num - cnt) + 1):
      stack.append(i + cnt)
      command.append('+')
    
    cnt += (num - cnt)
    
    stack.pop()
    command.append('-')
    
  else:
    command = ['NO']
    break

for comm in command:
  print(comm)