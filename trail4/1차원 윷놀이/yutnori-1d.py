n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
order = []
answer = 0


def calculate():
    score = [1] * (k)
    temp = 0
    for i in range(n):
        score[order[i]] += nums[i]
    for i in range(k):
        if score[i] >= m:
            temp += 1
    return temp

def backtrack(cur):
    global answer
    if cur == n:
        result = calculate()
        answer = max(answer, result)
        return
    
    for i in range(k):
        order.append(i)
        backtrack(cur + 1)
        order.pop()

backtrack(0)
print(answer)
