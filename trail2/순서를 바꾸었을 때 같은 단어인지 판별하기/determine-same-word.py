word1 = input()
word2 = input()

# Please write your code here.
word1_list = list(word1)
word2_list = list(word2)
word1_list.sort()
word2_list.sort()
flag = True

if len(word1_list) != len(word2_list):
    flag = False

if flag:
    for i in range(len(word1_list)):
        if word1_list[i] != word2_list[i]:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")