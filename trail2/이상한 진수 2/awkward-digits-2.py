a = list(input().rstrip())
answer = 0

def makeTen(binaryString):
    result = 0
    n = len(binaryString)
    for i in range(n):
        if binaryString[i] == '1':
            result += 2 ** (n - 1 - i)
    return result

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        answer = max(answer, makeTen(a))
        a[i] = '0'
    else:
        a[i] = '0'
        answer = max(answer, makeTen(a))
        a[i] = '1'

print(answer)