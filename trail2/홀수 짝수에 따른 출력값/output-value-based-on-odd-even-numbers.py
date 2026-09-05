N = int(input())

# Please write your code here.

def rec_sum(n):
    if n == N:
        return n
    
    return n + rec_sum(n+2)

if N % 2 == 0:
    print(rec_sum(2))
else:
    print(rec_sum(1))
