count = 0
answer = []
while True:
    word = input()
    if word == '0':
        break
    count += 1
    if count % 2 == 1:
        answer.append(word)
print(count)
for i in answer:
    print(i)