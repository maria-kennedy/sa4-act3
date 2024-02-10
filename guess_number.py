number = 10
number = 10
print("I'm thinking of a number...")
guess = 0
max_guesses = 5 
remaining_guesses = max_guesses

while remaining_guesses > 0:   
    
    guess = input("What number am I thinking of? (or q to exit) ")
    
    if guess == 'q':
        print(f"The number was {number}. \nBye!")
        break

    elif guess.isdigit():
        guess = int(guess)
        remaining_guesses -= 1

        if guess == number:
            print('Congratulations! You guessed the right number.')
            break
        elif guess < number: 
            print(f'Too low, {remaining_guesses} guesses left.')
        else:
            print(f'Too high, {remaining_guesses} guesses left.')

    if remaining_guesses == 0:
        print(f'Sorry, you have used all your guesses. The number was {number}.')
        break