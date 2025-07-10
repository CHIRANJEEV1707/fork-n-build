# Generate a random num
import random

# Specifying the range bt taking input
print('Please enter the range of numbers -')
min = int(input('Minimum : '))
max = int(input('Maximum : '))
num = random.randint(min,max)

# attempts
attempts = 5
guessed = 0

# loop
while True :
# take input guess
    try:
        print(f'You have only {attempts} attempts!')
        guess = int(input(f'Guess the number between {min} and {max} : '))

    # if num < guess : too low
        if guess < num : 
            print('Too low!')
            guessed += 1
            attempts -= 1
            if attempts == 0:
                print('Attempts Over!')
                print('Sorry! Try Next Time!')
                print(f'The number was {num}')
                break
            
    # if num > guess : too high
        elif guess > num :
            print('Too high!')
            guessed += 1
            attempts -= 1
            if attempts == 0:
                print('Attempts Over!')
                print('Sorry! Try Next Time!')
                print(f'The number was {num}.')
                break

    # else num == guess : well done 
        else :
            guessed += 1
            print(f'Congratulations! You guessed the number in {guessed} attempts!')
            break
        
    # if invalid num : error
    except ValueError:
        print('Please enter a valid number')
