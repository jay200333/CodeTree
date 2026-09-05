N = int(input())

# Please write your code here.

def rec_sum(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return rec_sum(n//2) + 1
    else:
        return rec_sum(n//3) + 1

print(rec_sum(N))