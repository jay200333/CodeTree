binary = input()

# Please write your code here.
answer = 0
for i in range(len(binary)):
    answer = answer * 2 + int(binary[i])
print(answer)