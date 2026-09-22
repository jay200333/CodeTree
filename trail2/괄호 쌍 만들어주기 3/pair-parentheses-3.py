A = input()

answer = 0
length = len(A)
for i in range(length - 1):
    for j in range(i+1, length):
        if A[i] == '(' and A[j] == ')':
            answer += 1

print(answer)