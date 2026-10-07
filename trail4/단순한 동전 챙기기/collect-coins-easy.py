n = int(input())
grid = [list(input()) for _ in range(n)]
start = None
end = None
numbers = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)
        elif grid[i][j].isdigit():
            numbers.append((int(grid[i][j]), i, j))

numbers.sort()
answer = int(1e9)

def calculate(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if len(numbers) < 3:
    print(-1)
else:
    num_length = len(numbers)
    for i in range(num_length):
        for j in range(i+1, num_length):
            for k in range(j+1, num_length):
                c1 = (numbers[i][1], numbers[i][2])
                c2 = (numbers[j][1], numbers[j][2])
                c3 = (numbers[k][1], numbers[k][2])

                total_dist = calculate(start, c1) + calculate(c1, c2) + calculate(c2, c3) + calculate(c3, end)
                answer = min(answer, total_dist)

    print(answer if answer != int(1e9) else -1)
