N, K = map(int, input().split())
candy = [0] * 101


answer = 0
for i in range(N):
    a, x = map(int, input().split())
    candy[x] += a

for i in range(201):
    start = max(0, i-K)
    end = min(i+K, 200)
    temp = sum(candy[start:end + 1])
    answer = max(answer, temp)

print(answer)