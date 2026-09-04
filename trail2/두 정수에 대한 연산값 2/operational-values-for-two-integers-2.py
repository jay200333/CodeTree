a, b = map(int, input().split())

# Please write your code here.
if a < b :
    a += 10
    b *= 2
else:
    a *= 2
    b += 10
print(a, b)