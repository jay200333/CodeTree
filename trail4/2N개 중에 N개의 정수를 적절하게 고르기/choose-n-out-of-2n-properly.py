import sys

n = int(input())
num = list(map(int, input().split()))
answer = sys.maxsize

def backtrack(cur, count, value):
    global answer
    if cur == len(num):
        if count == n:
            sum1 = value
            sum2 = sum(num) - value
            answer = min(answer, abs(sum1 - sum2))
        return
    
    backtrack(cur + 1, count + 1, value + num[cur])
    backtrack(cur + 1, count, value)

backtrack(0, 0, 0)
print(answer)
