answer = ""
n = input()
for i in n:
    if i.isdigit():
        answer += i
    elif i.isalpha():
        answer += i.lower()
print(answer)
