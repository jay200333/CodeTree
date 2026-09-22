A = input()

answer = 0
n = len(A)
for i in range(n):
    for j in range(i+2, n-1):
        if A[i] == '(' and A[i+1] == '(' and A[j] == ')' and A[j+1] == ')':
            answer += 1

print(answer)