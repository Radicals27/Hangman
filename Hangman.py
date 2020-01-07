import random

#Setup the images of hangman in a list
draw_hangman = ["""
          ---------
          |       |
          |       
          |
          |
          |
          |
          |_________________

""",
"""
          ---------
          |       |
          |       O
          |
          |
          |
          |
          |_________________

""",
"""
          ---------
          |       |
          |       O
          |       |
          |       |
          |
          |
          |_________________

""",
"""
          ---------
          |       |
          |       O
          |       |
          |       |
          |      /
          |
          |_________________

""",
"""
          ---------
          |       |
          |       O
          |       |
          |       |
          |      / \\
          |
          |_________________

""",
"""
          ---------
          |       |
          |       O
          |      /|
          |       |
          |      / \\
          |
          |_________________

""",
"""
          ---------
          |       |
          |       O
          |      /|\\
          |       |
          |      / \\
          |
          |_________________
"""]

#XXXXXXXXXXXXX??????
def letter_checker(letter):
    for y in guessed_letters:
        if y == letter:
            return True
    return False

#Check if all of the letters have been guessed correctly
def check_win():
    for y in mystery_word:
        if word_contains(guessed_letters, y):
            continue
        else:
            return False
    return True

#Check if a word (array) contains a particular character (char)
def word_contains(array, char):
    if char in array:
        return True
    else:
        return False

#Some sample words
words = ["elephant", "project", "kangaroo", "kitchen", "pineapple", "automobile", "instance", "butter", "jamaica"]
bad_guesses = 0   #This will increment as the player guesses incorrectly
guessed_letters = []  #A list holding all of the guessed letters
mystery_word = words[random.randint(0, len(words) - 1)]   #Choose a mystery word from the available words, at random

#Main game loop
while bad_guesses < 7:
    if(check_win()):    #Check for win condition
        print("YOU WIN!!!")

    print(draw_hangman[bad_guesses])  #Print the hangman image associated with the number of bad guesses
    for x in mystery_word:  #Display the underscores and guessed letters so far so the player can see their progress
        if letter_checker(x):
            print(x, end=" ")
        else:
            print(" _ ", end="")

    user_guess = input("\n Type a letter: ")  #Prompt the user for a letter
    if user_guess in mystery_word:  #If they guess a letter correctly
        print("Good guess! Wrong guesses made: ", bad_guesses)
        guessed_letters.append(user_guess)
        #break
    else:
        guessed_letters.append(user_guess)  #f user guessed incorrectly
        bad_guesses += 1
        print("Sorry, try again, bad guesses: ", bad_guesses)
