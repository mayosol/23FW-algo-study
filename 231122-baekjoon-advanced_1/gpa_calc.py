# sum(학점 * 과목평점) / sum(학점)

grade2rate = {
  'A+':	4.5,
  'A0':	4.0,
  'B+':	3.5,
  'B0':	3.0,
  'C+':	2.5,
  'C0':	2.0,
  'D+':	1.5,
  'D0':	1.0,
  'F':	0.0,
  'P': None
}

sum_credit_times_rate = 0
sum_credit = 0

for _ in range(20):
  credit, grade = input().split(' ')[1:]
  
  if grade == 'P':
    continue
  
  credit = float(credit)
  sum_credit += credit
  sum_credit_times_rate += (credit * grade2rate[grade])

print(sum_credit_times_rate/sum_credit)