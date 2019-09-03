# This is a guess the number game.
import random

secret_number = random.randint(0, 20)
guess_correct = False
print('I am thinking a number between 0 and 20')

# Ask the player to guess 6 times
for guess_time in range(1, 5):
    print('Take a guess')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        guess_correct = True
        break

if guess_correct:
    print('Good job! You guess my number in ' + str(guess_time) + ' times!')
else:
    print('Nope. The number I was thinking of is ' + str(secret_number))
