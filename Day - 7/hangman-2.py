word = input("Guess a word: ")
print(f"OK, so...the word is : {word}")

dashed_list = []
for w in word:
    dashed_list += "_"
print(dashed_list)

correct_count = 0
while (correct_count != len(word)):
    letter = input("Guess a letter: ")
    for i in range(len(word)):
        w = word[i]
        if letter == w:
            dashed_list[i] = letter
            correct_count += 1
    print(dashed_list)
print("You win")