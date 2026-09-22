n = int(input())
numbers = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(n):
        if abs(i-j) >= 2:
            answer = max(answer, numbers[i] + numbers[j])

print(answer)