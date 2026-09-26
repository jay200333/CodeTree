n = int(input())

answer = 0
result = []

def checkNum(temp):
    m = len(temp)
    i = 0
    
    while i < m:
        cur = temp[i]
        if cur + i > m:
            return False
    
        for j in range(cur):
            if temp[i+j] != cur:
                return False
    
        i += cur
    return True

def backtrack(cur):
    global answer
    if cur == n:
        if checkNum(result):
            answer += 1
        return
    
    for i in range(1,5):
        result.append(i)
        backtrack(cur + 1)
        result.pop()

backtrack(0)
print(answer)