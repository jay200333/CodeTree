answer = 0
n = input()
for i in n:
    if i.isdigit():
        answer += int(i)
print(answer)