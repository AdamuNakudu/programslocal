import random

number = random.randint(1, 10)
print('Guess the number from 1 to 10')

for guesses in range(1, 5):
    guess = int(input('Guess:'))

    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    else:
        break
if guess == number:
    print('You win!')
else: 
    print('You lose!')
    print('The number was:' + str(number))

