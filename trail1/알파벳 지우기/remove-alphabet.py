first = input()
second = input()

temp = ""
for i in first:
    if i.isdigit():
        temp += i

answer = int(temp)
temp = ""
for i in second:
    if i.isdigit():
        temp += i
answer += int(temp)
print(answer)