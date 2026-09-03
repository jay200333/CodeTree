n = input()
answer = ""
for i in n:
    if i.isalpha():
        answer += i.upper()
print(answer)
