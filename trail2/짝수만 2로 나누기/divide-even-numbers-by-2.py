n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
print(*[i // 2 if i % 2 == 0 else i for i in arr  ])