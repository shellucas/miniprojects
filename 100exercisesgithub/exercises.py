"""Question 1"""
import operator
import re
from math import sqrt


def get_divby7_notmulof5(lowbound, highbound):
    """Get a list of numbers divisible by 7, but not a multiple of 5.
        List is in range of low bound >= N >= high bound.
    """
    return [x for x in range(lowbound, highbound + 1) if x % 7 == 0 and x % 5 != 0]


# print(numbers)


"""Question 2"""


def factorial(x):
    """Computes the factorial using recursion of a given x"""
    if x == 0:
        return 1
    return x * (factorial(x - 1))


# number = int(input('Factorial of: '))
# print(factorial(number))


"""Question 3"""


def gen_squared_dict(high):
    """Returns a dictionary containing all squares up until high"""
    squared_dict = {}
    for x in range(1, high + 1):
        squared_dict[x] = x * x
    return squared_dict


# number = int(input('Integral number: '))
# print(gen_squared_dict(number))


"""Question 4"""


def str_to_list_and_tuple(sequence):
    """Returns a dictionary containing a list and a tuple containing all numbers
        in the passed sequence. Assuming sequence is a comma separated, string.
    """
    initial = sequence.split(',')
    converted = tuple(initial)
    return {'list': initial, 'tuple': converted}


# num_seq = input('Comma separated integers: ')
# print(str_to_list_and_tuple(num_seq).get('list'))
# print(str_to_list_and_tuple(num_seq).get('tuple'))


"""Question 5"""


class Uppercaser:

    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input('String: ')

    def print_string(self):
        print(self.string.upper())


# s = Uppercaser()
# s.get_string()
# s.print_string()


"""Question 6"""


def seq_to_formula(sequence):
    values = [int(x) for x in sequence.split(',')]
    q_dict = dict()
    c = 50
    h = 30
    for D in values:
        q_dict[str(D)] = int(sqrt((2 * c * D) / h))
    return q_dict


# int_seq = input('Comma separated integers: ')
# print(print_seq_to_formula(int_seq).values())


"""Question 7"""


def matrix(rows, columns):
    return [[j * i for j in range(columns)] for i in range(rows)]


# values = [int(x) for x in input('Row and Column separated: ').split(',')]
# for row in matrix(values[0], values[1]):
#     print(row)


"""Question 8"""


def sort_words(words):
    return sorted(words)


# values = input('Comma separated words: ').split(',')
# print(",".join(word for word in sort_words(values)))


"""Question 9"""


def cap_sentences(sentences):
    return [x.upper() for x in sentences]


# lines = []
# while True:
#     sentence = input('Sentence: ')
#     if sentence:
#         lines.append(sentence)
#     else:
#         break
#
# for x in cap_sentences(lines):
#     print(x)


"""Question 10"""


def unique_sorted(strings):
    return sorted(set(strings))


# words = input('Enter sequence of words: ').split(' ')
# print(' '.join(unique_sorted(words)))


"""Question 11"""


def binary_div_by_5(binaries):
    return [b for b in binaries if int(b, 2) % 5 == 0]


# bins = input('Comma separated binaries: ').split(',')
# print(','.join([str(x) for x in binary_div_by_5(bins)]))


"""Question 12"""


def even_digit_numbers(low, high):
    even_numbers = []
    for x in range(low, high + 1):
        str_num = str(x)
        is_even = True
        for digit in str_num:
            if int(digit) % 2 != 0:
                is_even = False
                break
        if is_even:
            even_numbers.append(int(str_num))
    return even_numbers


# print(','.join([str(x) for x in even_digit_numbers(1000, 3000)]))


"""Question 13"""


def count_letters_digits(line):
    d = {'Letters': 0, 'Digits': 0}
    for x in line:
        if x.isdigit():
            d['Digits'] += 1
        elif x.isalpha():
            d['Letters'] += 1
    return d


# string = input('Enter a string with digits and/or letters: ')
# dic = count_letters_digits(string)
# print('Letters:', dic['Letters'])
# print('Digits:', dic['Digits'])


"""Question 14"""


def count_upper_lower(line):
    d = {'upper': 0, 'lower': 0}
    for letter in line:
        if letter.isupper():
            d['upper'] += 1
        elif letter.islower():
            d['lower'] += 1
    return d


# string = input('Enter a string: ')
# dic = count_upper_lower(string)
# print('UPPER CASE:', dic['upper'])
# print('LOWER CASE:', dic['lower'])


"""Question 15"""


def compute_a(value):
    a = int(value)
    return (a
            + int(str(a) + str(a))
            + int(str(a) + str(a) + str(a))
            + int(str(a) + str(a) + str(a) + str(a)))


# print(compute_a(9))


"""Question 16"""


def odd_squared(line):
    return [x**2 for x in line if x % 2 != 0]


# s = [int(x) for x in input('Comma separated integers: ').split(',')]
# print(','.join(str(x) for x in odd_squared(s)))


"""Question 17"""


def transaction(account, trans):
    print(trans)
    for line in trans:
        t = line.split(' ')
        op = t[0].upper()
        amount = int(t[1])
        if op == 'D':
            account += amount
        elif op == 'W':
            account -= amount
    return account


# balance = 0
# transactions = []
# while True:
#     function = input('Enter a transaction (format = [D or W] + space + amount)')
#     if function:
#         transactions.append(function)
#     else:
#         break
#
# print(transactions)
# balance = transaction(balance, transactions)
# print(balance)


"""Question 18"""


def password_check(passwords):
    valid_passes = []
    for password in passwords:
        if len(password) < 6 or len(password) > 12:
            continue
        if not re.search('[a-z]', password):
            continue
        if not re.search('[0-9]', password):
            continue
        if not re.search('[A-Z]', password):
            continue
        if not re.search('[$#@]', password):
            continue
        valid_passes.append(password)
    return valid_passes


# line = input('Comma separated passwords: ').split(',')
# print(','.join(x for x in password_check(line)))


"""Question 19"""


def sort_tuples(people):
    return sorted(people, key=operator.itemgetter(0, 1, 2))


# people_list = [('Tom', 19, 80),
#                ('John', 20, 90),
#                ('Jony', 17, 91),
#                ('Jony', 17, 93),
#                ('Json', 21, 85)]
# print(sort_tuples(people_list))


"""Question 20"""


class DivisibleIter:

    def __init__(self, n, div=7):
        self.n = n
        self.div = div

    def __iter__(self):
        for x in range(self.n):
            if x % self.div == 0:
                yield x
            self.n = x


i = DivisibleIter(100)
for d in i:
    print(d)

for d in i:
    print(d)
