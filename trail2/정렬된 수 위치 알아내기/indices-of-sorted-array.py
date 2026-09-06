n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
numbers = [(i, sequence[i]) for i in range(n)]
numbers.sort(key=lambda x: x[1])

answer = [0] * n
for i, number in enumerate(numbers):
    answer[number[0]] = i

for i in range(n):
    print(answer[i]+1, end=" ")