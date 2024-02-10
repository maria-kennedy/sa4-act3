number = '10'
print("I'm thinking of a number...")
guess = 0

while guess != 'q':   
    
    guess = input("What number am I thinking of? (or q to exit) ")
    
    if guess == 'q':
        print(f"The number was {number}. \nBye!")
        break

    elif guess == number:
        print("Congratulations! You guessed the right number.")
        break
    
    else:
        print("Try again!")