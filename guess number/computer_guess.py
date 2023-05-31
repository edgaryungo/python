# computer has a secret number and we try to guess

import random


def guess(x):
    secret_number = random.randint(1, x)
    guess = 0

    while guess != secret_number:
        guess = int(input(f'Guess the number between 1 and {x}: '))

        if guess < secret_number:
            print('Your guess is too low')
        elif guess > secret_number:
            print('Your guess is too high')
    print(f'Youve guessed {secret_number} correctly')

# come up with a number and have the computer to guess it
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0

    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} too High (H), too low (L) or Correct (C):').upper()
        count += 1

        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print(f'I guessed {guess} correctly after {count} trials')


# guess(10)
computer_guess(1000)

