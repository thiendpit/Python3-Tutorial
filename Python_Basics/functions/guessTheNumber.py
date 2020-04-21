# this is a guess the number game
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# ask the player to guess 5 times
for i in range(1, 6):
  print('Take a guess.')
  guess = int(input())

  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is to high.')
  else:
    break 

if guess == secretNumber:
  print('Good job! You guessed my number in ' + str(guess) + ' guesses!')
else:
  print('Nope. The number I was thinking of was ' + str(secretNumber))