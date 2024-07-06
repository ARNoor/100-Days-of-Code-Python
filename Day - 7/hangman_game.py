import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



print("========= Welcome to the HANGMAN GAME =========")
word = input("The word: ")

def make_dashed_list():
    dashed_list = []
    for _ in word:
        dashed_list += "_"
    print(dashed_list)
    return dashed_list

dashed_list = make_dashed_list()
curr_marker = len(stages) - 1

while curr_marker > 0:
    correct_guess = False
    guessed_letter = input("Guess a letter: ")

    for i in range(len(word)):
        if guessed_letter == word[i]:
            dashed_list[i] = guessed_letter
            correct_guess = True
            break

    if not correct_guess:
        curr_marker -= 1
        
    print(dashed_list)
    print(stages[curr_marker])    
    if(curr_marker == 0):
        print("Game over\n")
        break
    if("_" not in dashed_list):
        print("You win\n")
        break
