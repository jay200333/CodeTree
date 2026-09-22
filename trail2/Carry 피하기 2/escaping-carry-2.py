n = int(input())
arr = [int(input()) for _ in range(n)]

def carry(a, b):
    numberA = str(a)
    numberB = str(b)
    if len(numberA) > len(numberB):
        numberB = '0' * (len(numberA) - len(numberB)) + numberB
    else:
        numberA = '0' * (len(numberB) - len(numberA)) + numberA
    
    for i in range(len(numberA)):
        for j in range(len(numberB)):
            if i ==j and (int(numberA[i]) + int(numberB[i])) >= 10:
                return True
    return False


answer = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not carry(arr[i], arr[j]):
                temp = arr[i] + arr[j]
                if not carry(temp, arr[k]):
                    answer = max(answer, temp + arr[k])

print(answer)
