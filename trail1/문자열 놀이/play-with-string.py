s, q = input().split()

answer = list(s)
for _ in range(int(q)):
    a, b, c = input().split()
    if int(a) == 1:
        answer[int(b)-1], answer[int(c)-1] = answer[int(c)-1], answer[int(b)-1]
    elif int(a) == 2:
        for i in range(len(answer)):
            if answer[i] == b:
                answer[i] = c
    print("".join(answer))
