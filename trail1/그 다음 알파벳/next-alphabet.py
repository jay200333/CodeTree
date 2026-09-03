c = input()
print(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))