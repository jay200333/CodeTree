N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
tempB = sorted(B)
for i in range(N - M + 1):
    tempA = sorted(A[i:i+M])
    if tempA == tempB:
        answer += 1
print(answer)
