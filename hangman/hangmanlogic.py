import random


def _init_dictionary():
    word_list = []
    with open('words', 'r') as dictionary:
        for word in dictionary.readlines():
            word_list.append(word)
    return word_list


class Hangman:
    """A classic CLI version of hangman. To play call self.play()"""

    def __init__(self):
        self.attempts = 10
        self.dictionary = _init_dictionary()
        self.word = random.choice(self.dictionary)[:-1]
        self.guessed_letters = []
        self.hidden_word = ''
        for _ in self.word:
            self.hidden_word += '_'

    def play(self):
        """The only method needing to be called to play the game."""
        print('=============Welcome to Hangman!=============')
        while self.attempts != 0 and self.hidden_word != self.word:
            self._print_status()
            self._guess_letter()
        else:
            print()
            if self.attempts == 0:
                print('Unlucky, You didn\'t guess the word.\n'
                      'The answer was \'' + self.word + '\'.')
            else:
                print('Congratulations!! You guessed', self.word)

    def _print_status(self):
        """Prints the current status of the game."""
        print()
        print('The word I\'m thinking of has', len(self.word), 'letters.')
        if self.guessed_letters:
            print('Guessed letters are: ', self.guessed_letters)
        print('Word:     ', self.hidden_word, '     Attempts:', self.attempts)
        print()

    def _guess_letter(self):
        """Loops until the users inputs a valid letter."""
        while True:
            guess = input('Guess > ')
            if len(guess) != 1:
                print('Please only enter 1 letter.')
            elif guess in self.guessed_letters:
                print('You already guessed ' + guess)
            else:
                break
        self._update_status(guess)

    def _update_status(self, guess):
        """Updates the status of the game."""
        self.guessed_letters.append(guess)
        if guess not in self.word:
            print('Incorrect!')
            self.attempts -= 1
        self._update_hidden_word()

    def _update_hidden_word(self):
        """Updates the hidden word of the current game."""
        self.hidden_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                self.hidden_word += letter
            else:
                self.hidden_word += '_'
