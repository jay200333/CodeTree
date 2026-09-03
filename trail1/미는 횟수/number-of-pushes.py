a = input()
b = input()

for i in range(1, len(a)):
    if a[-i:] + a[:-i] == b:
        print(i)
        break
else:
    print(-1)