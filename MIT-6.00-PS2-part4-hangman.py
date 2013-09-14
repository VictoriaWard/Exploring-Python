# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# MIT Open Courseware - Introduction to Computer Science and Programming
# Problem Set 1 - part 4 - Hangman
# by Victoria Ward

"""
Problem #4
Implement a function, hangman(), that will start up and carry out an
interactive Hangman game between a player and the computer.
"""

"""
Requirements
Here are the requirements for your game:
1. The computer must select a word at random from the list of
available words that was provided in words.txt. The functions for
loading the word list and selecting a random word have already been
provided for you in ps2_hangman.py.
2. The game must be interactive: it should let a player know how many
letters the word the computer has picked contains and ask the user to
supply guesses. The user should receive feedback immediately after
each guess. You should also display to the user the partially guessed
word so far, as well as either the letters that the player has already
guessed or letters that the player has yet to guess.
3. A player is allowed some number of guesses. Once you understand how
the game works, pick a number that seems reasonable to you. Make sure
to remind the player of how many guesses s/he has left after each
turn.
4. A player loses a guess only when s/he guesses incorrectly.
5. The game should end when the player constructs the full word or
runs out of guesses. If the player runs out of guesses (s/he “loses”),
reveal the word to the player when the game ends.
"""

import random
import string

f = "words.txt"

def load_words():
    """
    Returns a list of valid . Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    inFile = open(f, 'r')
    line = inFile.readline()
    wordlist = (str.split(line))
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# your code begins here:


def display_word(word):
    """ display_word(str) -> list

    >>> display_word("hello")
    [' __ ', ' __ ', ' __ ', ' __ ', ' __ ']
    >>> display_word("hamburger")
    [' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ']

    Returns a list containing one blank letter space for each letter of a given word.
    """
    
    for l in word:
        word_frame.append(" __ ")
    return word_frame


def check_letter(letter, word):
    """ check_letter(str, str) -> Boolean

    >>> check_letter("h", "hello")
    True
    >>> check_letter("a", "hello")
    False

    Returns true if a given letter is in a given word.
    """
    
    return letter in word


def update_dis(letter, word, word_frame):
    """ update_dis("str", "str", list) -> list

    >>> update_dis("h", "hello", [' __ ', ' __ ', ' __ ', ' __ ', ' __ '])
    ['h', ' __ ', ' __ ', ' __ ', ' __ ']
    >>> update_dis("p", "happy", [' __ ', ' __ ', ' __ ', ' __ ', ' __ ')
    [' __ ', ' __ ', 'p', 'p', ' __ ']
    >>> update_dis("e", "repellent", [' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ ', ' __ '])
    [' __ ', 'e', ' __ ', 'e', ' __ ', ' __ ', 'e', ' __ ', ' __ ']

    Returns an updated word_frame list where the given letter replaces the blank letter space.

    Assumes that letter is in word.
    """

    word_frame[word.find(letter)] = letter
    if word.count(letter) > 1:
        index = word.find(letter)
        for c in range(word.count(letter) - 1):
            word_frame[word.find(letter, index +1)] = letter
            index = word.find(letter, index +1)
    return word_frame


def update_guessed(letter, guessed_letters):
    """ update_guessed("str", list) -> list

    >>> update_guessed("a", [])
    ["a"]
    >>> update_guessed("y", ['a', 'd'])
    ['a', 'd', 'y']

    Adds guessed letter to list of already guessed letters.
    """
    
    guessed_letters.append(letter)
    return guessed_letters
    

def print_guessed(guessed_letters):
    """ print_guessed(list) -> str

    >>> print_guessed(['a', 'd', 'y'])
    'a d y'

    Prints each letter in guessed_letters list.
    """

    guessed_string = ""
    for l in guessed_letters:
        guessed_string += l + " "
    return (guessed_string)
    

def hangman():
    word = choose_word(wordlist)
    word_frame = display_word(word)
    num_guesses = 10
    guessed_letters = []
    print ("The word is " + str(len(word)) + " letters.")
    print ("\n", word_frame)

    while num_guesses > 0:
        letter = str.lower(input("\nGuess a letter: "))
        while letter in guessed_letters:
            letter = str.lower(input("\nYou've already guessed that letter. Guess another letter: "))
        if check_letter(letter, word):
            print ("\nGood guess!")
            update_dis(letter, word, word_frame)
            if ' __ ' not in word_frame:
                print ("\nYou win!")
                print ("\n", word_frame)
                break
        else:
            print ("\nNo '" + letter + "'s! Sorry!")
            num_guesses -= 1
            print ("\nYou have " + str(num_guesses) + " guesses left.")
        guessed_letters = update_guessed(letter, guessed_letters)
        print ("\n", word_frame)
        print ("\nHere are the letters you've guessed so far: '" + print_guessed(guessed_letters) + "'")
        
    if num_guesses == 0:
        print ("\nYou lose!")
        print ("\nThe word was: " + str.upper(word) + "!")
    
wordlist = load_words()
word_frame = []

hangman()
