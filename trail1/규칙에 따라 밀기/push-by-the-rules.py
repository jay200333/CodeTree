n = input()
command = list(input())

for c in command:
    if c == 'L':
        n = n[1:] + n[0]
    elif c == 'R':
        n = n[-1] + n[:-1]
print(n)