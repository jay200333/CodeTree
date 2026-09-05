N = int(input())

# Please write your code here.
def rec_sum(n):
    if n < 10:
        return n**2
    return rec_sum(n//10) + (n % 10) **2

print(rec_sum(N))