text = input()
pattern = input()

# Please write your code here.
if pattern in text:
    print(text.index(pattern))
else:
    print(-1)