n = int(input())
A = list(map(int, input().split()))

answer = int(1e9)
for cur in range(n):
    distance = 0
    for j in range(n):
        if cur == j: continue
        distance += abs(cur - j) *A[j]
    answer = min(answer, distance)
print(answer)