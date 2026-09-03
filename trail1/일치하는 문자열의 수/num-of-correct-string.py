n, a = input().split()
answer = 0
for _ in range(int(n)):
    if input() == a:
        answer += 1
print(answer)