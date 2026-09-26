n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
arr = []
answer = int(1e9)
visited = [False] * (n+1)

def calculate():
    if A[0][arr[0] - 1] == 0:
        return int(1e9)
    distance = A[0][arr[0] - 1]
    for i in range(len(arr) - 1):
        start = arr[i] - 1
        end = arr[i+1] - 1
        if A[start][end] == 0:
            return int(1e9)
        distance += A[start][end]
    
    if A[arr[-1] - 1][0] == 0:
        return int(1e9)
    distance += A[arr[-1] - 1][0]
    return distance

def backtrack(cur):
    global answer
    if cur == n - 1:
        result = calculate()
        answer = min(answer, result)
        return

    for i in range(2, n + 1):
        if visited[i]: continue
        visited[i] = True
        arr.append(i)
        backtrack(cur + 1)
        arr.pop()
        visited[i] = False

backtrack(0)
print(answer)
