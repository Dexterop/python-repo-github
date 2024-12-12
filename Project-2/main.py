import random

# Generate a random number between a specified range 
actual_number = random.randint(1, 10)


guesses = 0

def Game():
    print("Welcome to the Perfect Guess!")

    global guesses
    while True:
        player_guess = int(input("What is Your Guess(Guess from 1-10) : "))

        guesses +=1
       

        if(player_guess > actual_number):
            print("Lower number please")
            print("Guess Again!")

        elif(player_guess < actual_number):
            print("Higher number please")
            print("Guess Again!")

        else:
            print(f"You Guessed the correct number {actual_number} in {guesses} attempts!")
            break
    
    print("Thanks for playing!")

Game()