N = int(input())

# Please write your code here.
def rec_sum(i):
    if i == 1:
        return 2
    if i == 2:
        return 4
    return rec_sum(i-1) * rec_sum(i-2) % 100

print(rec_sum(N))