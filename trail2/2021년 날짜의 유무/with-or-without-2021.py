M, D = map(int, input().split())

# Please write your code here.
month = {1:31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if M in range(1, 13) and D <= month[M]:
    print("Yes")
else:
    print("No")