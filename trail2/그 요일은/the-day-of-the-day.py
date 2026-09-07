m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = { 1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

totalDays = 0
if m2 > m1:
    totalDays += days[m1] - d1 + 1
    for i in range(m1+1, m2):
        totalDays += days[i]
    totalDays += d2
else:
    totalDays = d2 - d1 + 1

index = day[A]


answer = totalDays // 7
if index < (totalDays % 7):
    answer += 1
print(answer)