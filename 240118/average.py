n = int(input())
score = list(map(int, input().split()))
  
M = max(score)
new_score = [x / M * 100 for x in score]

print(sum(new_score) / len(new_score))
