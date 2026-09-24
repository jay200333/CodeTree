n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i+1, n+1):
        result = arr[i:j]
        avr = sum(result) / (j-i)
        if avr in result:
            answer += 1

print(answer)
