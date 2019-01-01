"""Question 1"""
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


def print_formula(sequence):
    values = [int(x) for x in sequence.split(',')]
    q_dict = dict()
    c = 50
    h = 30
    for D in values:
        q_dict[str(D)] = int(sqrt((2 * c * D) / h))
    return q_dict


int_seq = input('Comma separated integers: ')
print(print_formula(int_seq).values())


"""Question 7"""

