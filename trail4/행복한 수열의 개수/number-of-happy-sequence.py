n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
def check_happy_list(numbers):
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    if count >= m:
        return True
    return False

for i in range(n):
    if check_happy_list(grid[i]):
        answer += 1
    col = []
    for j in range(n):
        col.append(grid[j][i])
    if check_happy_list(col):
        answer += 1
print(answer)
