m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
totalDays = 0

def num_of_days(m, d):
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]
    
    total_days += d
    
    return total_days    

diff = num_of_days(m2, d2) - num_of_days(m1, d1)
while diff < 0:
    diff += 7

print(day[diff % 7])