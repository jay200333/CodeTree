import sys

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
arr = []

def calculate():
    temp = 0
    for i in range(m):
        for j in range(i+1, m):
            temp = max(temp, ((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2))
    return temp

def backtrack(idx):
    global answer
    if idx == n:
        if len(arr) == m:
            result = calculate()
            answer = min(answer, result)
        return
    
    arr.append(points[idx])
    backtrack(idx + 1)
    arr.pop()
    backtrack(idx + 1)

backtrack(0)
print(answer)

