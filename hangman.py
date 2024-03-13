import random
from wordlist import *


class Hangman:
    """Class for Hangman Game. User guesses until the word is fully guessed."""

    def __init__(self):
        self.guess_list = ''
        self.count = 0

    def clear_guess_list(self):
        """Clear the list of guesses"""
        self.guess_list = ''

    def guess(self, guess):
        """Return an error message if guess is invalid, else adds guess to guess_list and return nothing."""
        # If guess is more than one letter or not of valid characters, return appropriate message.
        if len(guess) > 1:
            reply = 'Make one guess at a time.'
            return reply
        if not guess.isalpha():
            reply = 'Please input valid characters.'
            return reply

        # else, add to guess list or notify if duplicated guess.
        guess = guess.upper()
        if guess not in self.guess_list:
            self.guess_list += guess

        else:
            reply = 'Repeated guess. Make another guess: '
            return reply

    def get_word(self):
        """Get a random word and hint from the library."""
        random_word, hint = random.choice(list(hangman_words.items()))
        return random_word, hint

    def display(self, random_word):
        """Display the word after each guess with _ for unguessed characters."""
        display_word = ''
        random_word = random_word.upper()
        for i in range(len(random_word)):
            if random_word[i] in self.guess_list:
                display_word += random_word[i]
            elif random_word[i] == ' ':
                display_word += ' '
            else:
                display_word += '_'
        return display_word

    def calc_count(self, word):
        dict = {}
        for char in word:
            if char not in dict:
                dict[char] = 1
            else:
                pass
        return len(dict) + 5
