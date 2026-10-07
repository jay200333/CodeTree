n, m = map(int, input().split())
A = list(map(int, input().split()))
answer = 0

def backtrack(idx, cur, value):
    global answer
    if idx == n:
        if cur == m:
            answer = max(answer, value)
        return
    
    backtrack(idx + 1, cur + 1, value ^ A[idx])
    backtrack(idx + 1, cur, value)

backtrack(0, 0, 0)
print(answer)