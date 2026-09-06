n = int(input())

score = []

for _ in range(n):
    student_input = input().split()
    score.append((student_input[0], int(student_input[1]), int(student_input[2]), int(student_input[3])))

# Please write your code here.
score.sort(key = lambda x: x[1] + x[2] + x[3])
for i in score:
    print(*i)