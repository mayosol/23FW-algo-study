def search(list, target):
  mn = 0
  mx = len(list) - 1
  
  while mn <= mx:
    center = (mn + mx) // 2
    
    if target == list[center]:
      return True
    
    if target > list[center]:
      mn = center + 1
    else:
      mx = center - 1
  
  return False


n = int(input())
n_nums = sorted(list(map(int, input().split())))

m = int(input())
m_nums = list(map(int, input().split()))

for m_n in m_nums:
  if search(n_nums, m_n):
    print(1)
  else:
    print(0)