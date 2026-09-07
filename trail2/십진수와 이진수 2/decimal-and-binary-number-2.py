N = input()

# Please write your code here.
number = 0
answer = ""
for i in range(len(N)):
    number = number * 2 + int(N[i])
number *= 17
while number > 0:
    answer += str(number % 2)
    number //= 2
print(answer[::-1])