a, b = map(int, input().split())

# Please write your code here.
answer = 0

for i in range(a, b+1):
    count = 0
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            count += 1
        if count >= 1:
            break
    else:
        answer += i
print(answer)