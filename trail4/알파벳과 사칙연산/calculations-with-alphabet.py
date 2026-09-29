from collections import deque

expression = input()
n = len(expression) // 2 + 1
op = []
alpha = []
numbers = []
answer = -int(1e9)
for i in expression:
    if i in ['-', '*', '+']:
        op.append(i)
    else:
        alpha.append(i)

def calculate():
    dict = {}
    for i in range(6):
        dict[chr(97 + i)] = numbers[i]
    idx = 0
    num = [ dict[i] for i in alpha]
    queue = deque(num)
    while len(queue) > 1:
        first = queue.popleft()
        second = queue.popleft()
        opt = op[idx]
        temp = 0
        if opt == '*':
            temp = first * second
        elif opt == '+':
            temp = first + second
        elif opt == '-':
            temp = first - second
        queue.appendleft(temp)
        idx += 1
    return queue[0]

def backtrack(cur):
    global answer
    if cur == 6:
        result = calculate()
        answer = max(answer, result)
        return
    
    for i in range(1, 5):
        numbers.append(i)
        backtrack(cur + 1)
        numbers.pop()

backtrack(0)
print(answer)
