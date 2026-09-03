A = input()
B = input()

# Please write your code here.
while A.find(B) != -1:
    idx = A.find(B)
    A = A[:idx] + A[idx+len(B):]
print(A)