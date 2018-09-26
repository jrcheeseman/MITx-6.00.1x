# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/JakeCheeseman/Documents/Dropbox/MITx-6.00.1x/L6 - Dictionaries/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ''
    for i in secretWord:
        if i in lettersGuessed:
            string = string + i
        else:
            string = string + '_ '
    return string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = ''
    import string
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            letters = letters + i
    return letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')

    guessesLeft = 8
    lettersGuessed = []

    while guessesLeft > 0 or isWordGuessed(secretWord, lettersGuessed) == False:

        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        print('Please guess a letter: ', end=' ')
        guess = str(input())
        lettersGuessed.append(guess)

        if guess in secretWord:
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                print('Congratulations, you won!')
                break
            elif len(lettersGuessed) > 1 and guess in lettersGuessed[:-1]:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
            else:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
        elif len(lettersGuessed) > 1 and guess in lettersGuessed[:-1]:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        elif guess not in secretWord:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            guessesLeft -= 1
            if guessesLeft == 0:
                print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
                break


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
