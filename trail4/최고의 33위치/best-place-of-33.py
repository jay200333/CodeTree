n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for i in range(n-3+1):
    for j in range(n-3+1):
        count = 0
        for k in range(3):
            for l in range(3):
                if grid[i+k][j+l]:
                    count +=1
        answer = max(answer, count)
print(answer)