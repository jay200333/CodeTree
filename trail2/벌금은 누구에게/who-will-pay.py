N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
answer = -1
fault = [K] * (N+1)

for i in range(M):
    fault[student[i]] -= 1
    if fault[student[i]] == 0:
        answer = student[i]
        break

print(answer)
