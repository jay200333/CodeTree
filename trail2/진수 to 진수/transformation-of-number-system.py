a, b = map(int, input().split())
n = input()
number = 0
# Please write your code here.
if n == "0":
    print(0)
else:
    for i in range(len(n)):
        number = number * a + int(n[i])

    answer = ""
    while number > 0:
        answer += str(number % b)
        number //= b
    print(answer[::-1])