a, b = map(int, input().split())

# Please write your code here.
if a > b:
    a += 25
    b *= 2
elif a < b:
    a *= 2
    b += 25

print(a, b)