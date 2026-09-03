input_string = input()
input_string_list = list(input_string)
input_string_list[1] = 'a'
input_string_list[-2] = 'a'
print("".join(input_string_list))