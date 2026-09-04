n = int(input())

# Please write your code here.
if n % 2 == 0 and sum(list(map(int,str(n)))) % 5 == 0:
    print("Yes")
else:
    print("No")