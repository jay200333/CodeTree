answer = ""
n = input()
for i in n:
    if i.islower():
        answer += i.upper()
    elif i.isupper():
        answer += i.lower()
print(answer)