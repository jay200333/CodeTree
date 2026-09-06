unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
line_info = (unlock_code, wire_color, seconds)

print(f"code : {line_info[0]}")
print(f"color : {line_info[1]}")
print(f"second : {line_info[2]}")