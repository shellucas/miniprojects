import random


def _init_dictionary():
    word_list = []
    with open('words', 'r') as dictionary:
        for word in dictionary.readlines():
            word_list.append(word)
    return word_list


class Hangman:

    def __init__(self):
        self.max_tries = 5
        self.current_tries = 0
        self.dictionary = _init_dictionary()
        self.word = random.choice(self.dictionary)[:-1]
        self.guessed_letters = []
        self.hidden_word = ''

    def play(self):
        print(self.dictionary)
        print(self.word)
        print('=============Welcome to Hangman!=============')
        while self.word != self.hidden_word or self.current_tries == self.max_tries:
            self._print_status()
            self._guess_letter()

        if self.current_tries == self.max_tries:
            print('Unlucky, You didn\'t guess the word.\n'
                  'The answer was \'', self.word, '\'.')
        else:
            print('Congratulations!! You guessed', self.word)

    def _print_status(self):
        print()
        print('The current word has', len(self.word), 'letters.')
        print('Guessed letters are: ', self.guessed_letters)
        self.hidden_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                self.hidden_word += letter
            else:
                self.hidden_word += '_'
        print('Word:     ', self.hidden_word, '     Tries:', self.current_tries)
        print()

    def _guess_letter(self):
        while True:
            guess = input('Guess > ')
            if len(guess) != 1:
                print('Please only enter 1 letter')
            elif guess in self.guessed_letters:
                print('You already guessed ' + guess)
            else:
                break
        self.guessed_letters.append(guess)
        if guess not in self.word:
            self.current_tries += 1
