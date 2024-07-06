import random

words_list = ["ardvark", "baboon", "camel"]
#word = words_list[random.randint(0, len(words_list)-1)]
word = random.choice(words_list)

letter = input("Guess a letter: \n")
for w in word:
    if w == letter:
        print("Right")
    else:
        print("Wrong")