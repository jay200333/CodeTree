n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def max_rec(i):
    if i == n-1:
        return arr[i]
    return max(max_rec(i+1), arr[i])

print(max_rec(0))