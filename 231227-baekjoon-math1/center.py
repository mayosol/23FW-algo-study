num_iter = int(input())

points = 2

# for exp in range(num_iter):
#   points += 2**exp

# print(points**2)

for exp in range(num_iter):
  points += points - 1

print(points**2)