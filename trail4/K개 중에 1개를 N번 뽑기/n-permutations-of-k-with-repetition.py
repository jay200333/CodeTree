K, N = map(int, input().split())
result = []

def backtrack(cur):
    if cur == N:
        print(*result)
        return
    
    for i in range(1, K+1):
        result.append(i)
        backtrack(cur + 1)
        result.pop()

backtrack(0)

