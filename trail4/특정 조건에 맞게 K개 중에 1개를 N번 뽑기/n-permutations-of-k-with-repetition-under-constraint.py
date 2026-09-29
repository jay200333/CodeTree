K, N = map(int, input().split())

result = []

def backtrack(cur):
    if cur >= 3 and (result[-1] == result[-2]) and (result[-2] == result[-3]):
            return
    if cur == N:
        print(*result)
        return

    for i in range(1, K + 1):
        
        result.append(i) 
        backtrack(cur + 1)
        result.pop()

backtrack(0)