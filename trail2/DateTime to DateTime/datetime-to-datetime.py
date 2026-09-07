a, b, c = map(int, input().split())

# Please write your code here.
totalMinutes = a * 60 * 24 + b * 60 + c
baseMinutes = 11 * 60 * 24 + 11 * 60 + 11

if baseMinutes > totalMinutes:
    answer = -1
else:
    answer = totalMinutes - baseMinutes
print(answer)