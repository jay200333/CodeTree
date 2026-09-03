input_string = list(input())
while True:
    if len(input_string) == 1:
        break
    n = int(input())
    if n >= len(input_string):
        input_string.pop(-1)
    else:
        input_string.pop(n)
    print("".join(input_string))
