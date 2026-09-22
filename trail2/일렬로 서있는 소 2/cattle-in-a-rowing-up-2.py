N = int(input())
A = list(map(int, input().split()))

answer = 0
length = len(A)
for i in range(length - 2):
    for j in range(i+1, length - 1):
        for k in range(j + 1, length):
            if A[i] <= A[j] and A[j] <= A[k]:
                answer += 1

print(answer)