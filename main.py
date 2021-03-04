import random

import Hangmanlogo
import Stages
import Words

display = []

lives = 6

chosen_word = random.choice(Words.word_list)
word_length = len(chosen_word)

#this part is not mine, had help
for _ in range(word_length):
    display += "_"

print(Hangmanlogo.logo)
print(chosen_word)
while chosen_word is not True:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Letter is already chosen, try again")

    #this part is not mine, had help
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess in chosen_word:
        print(lives)
    elif guess not in chosen_word:
        lives = lives - 1
        print(lives)
        if lives == 0:
            chosen_word = True
            print("You lose")

    if lives == 5:
        print(Stages.stages[5])
    elif lives == 4:
        print(Stages.stages[4])
    elif lives == 3:
        print(Stages.stages[3])
    elif lives == 2:
        print(Stages.stages[2])
    elif lives == 1:
        print(Stages.stages[1])
    elif lives == 0:
        print(Stages.stages[0])

    if "_" not in display:
        chosen_word = True
        print("You win")