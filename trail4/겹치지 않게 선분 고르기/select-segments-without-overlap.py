n = int(input())
x1, x2 = [], []
result = []
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

def calculate():
    visited = [False] * 1001
    m = len(result)
    for i in range(m):
        idx = result[i]
        s, e = x1[idx], x2[idx]
        for j in range(s, e+1):
            if visited[j]:
                return 0
            visited[j] = True
    return m

def backtrack(cur):
    global answer
    if cur == n:
        count = calculate()
        answer = max(answer, count)
        return
    
    result.append(cur)
    backtrack(cur+1)
    result.pop()
    backtrack(cur+1)

backtrack(0)
print(answer)