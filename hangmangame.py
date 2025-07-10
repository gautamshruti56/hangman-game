# Hangman Game in Python
# A simple console-based hangman game where the player guesses letters to reveal a hidden word.


import random


word_list = ['apple', 'robot', 'chair', 'house', 'plant'] # Add more words as needed
word_to_guess = random.choice(word_list)
guessed_letters = []
tries = 6


print("🎮 Welcome to Hangman!")
print("_ " * len(word_to_guess))

while tries > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue


    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!") 


        if all(letter in guessed_letters for letter in word_to_guess):
            print("\n You won! The word was:", word_to_guess)
            break
    else:
        tries -= 1
        print("Incorrect guess. Tries left:", tries)


    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Current word:", display_word.strip())


if tries == 0:
    print("\n You lost. The word was:", word_to_guess) 
