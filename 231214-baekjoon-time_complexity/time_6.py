# def menOfPassion(A, n):
#   sum <- 0
#   for i in range(0, n-2): 
#     for j in range(i+1, n-1):
#       for k in range(j+1, n):
#         sum += A[i] * A[j] * A[k] 
#   return sum

# def counter(n):
#   sum = 0
#   for i in range(0, n-2): 
#     for j in range(i+1, n-1):
#       for k in range(j+1, n):
#         sum += 1
#   return sum

n = int(input())

# num = 0

# for i in range(1, n-1):
#   num += i**2 + i

# print(num//2)
# print(3)

print( (n**3 - (5*n**2) + (6*n) + 1)//2 )
print(3)