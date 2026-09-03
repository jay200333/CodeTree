n = int(input())
total = 0
for _ in range(n):
    total += int(input())
answer = str(total)
answer = answer[1:] + answer[0]
print(answer)