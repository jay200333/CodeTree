word = input()

if len(word) >= 2:
    word1 = word[0]
    word2 = word[1]
    word = "".join([word2 if c == word1 else (word1 if c == word2 else c) for c in word])

print(word)