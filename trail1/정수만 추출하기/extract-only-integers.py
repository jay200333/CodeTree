a, b = input().split()
answer = 0

temp = ""
for i in a:
    if i.isdigit():
        temp += i
    else:
        break
answer += int(temp)
temp = ""

for i in b:
    if i.isdigit():
        temp += i
    else:
        break
answer += int(temp)
print(answer)