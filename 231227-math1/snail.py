A, B, V = map(int, input().split(' '))

days = (V - B) // (A - B)

print(days+1) if (V - B) % (A - B) != 0 else print(days)
