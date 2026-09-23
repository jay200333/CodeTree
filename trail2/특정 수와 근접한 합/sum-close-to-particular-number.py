N, S = map(int, input().split())
arr = list(map(int, input().split()))

numberSum = sum(arr)
answer = int(1e9)

for i in range(N-1):
    for j in range(i+1, N):
        temp = arr[i] + arr[j]
        answer = min(answer, abs((numberSum - temp) - S))

print(answer)
