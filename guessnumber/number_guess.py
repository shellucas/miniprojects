import random

low = 1
high = 100

answer = random.randint(low, high + 1)
question = 'Guess a number between 1-100: '

tries = 0

guess = 0
while guess != answer:
    tries += 1
    guess = int(input(question))
    if guess < answer:
        print('Too low')
    if guess > answer:
        print('Too high')

print('Congratulations! The correct answer was', guess,
      'You guessed it in', tries, 'tries')
