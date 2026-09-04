n = int(input())

# Please write your code here.
def rec1(i):
    if i == n+1:
        return
    print(i, end=" ")
    rec1(i+1)

def rec2(i):
    if i == 0:
        return
    print(i, end=" ")
    rec2(i-1)

rec1(1)
print()
rec2(n)