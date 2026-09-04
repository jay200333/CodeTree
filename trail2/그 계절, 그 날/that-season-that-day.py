Y, M, D = map(int, input().split())

# Please write your code here.
month = {1:31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
    month[2] = 29

if M in range(1, 13) and D <= month[M]:
    if M in range(3, 6):
        print("Spring")
    elif M in range(6, 9):
        print("Summer")
    elif M in range(9, 12):
        print("Fall")
    elif M in [12, 1, 2]:
        print("Winter")
else:
    print(-1)