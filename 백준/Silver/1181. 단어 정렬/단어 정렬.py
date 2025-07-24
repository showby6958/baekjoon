N = int(input())
words = set()
i = 0

while True:
    try:
        word = input()
        if word == "":
            break
        words.add(word)
    except EOFError:
        break

sorted_words = sorted(words, key=lambda x : (len(x), x))

for w in sorted_words:
    print(w)