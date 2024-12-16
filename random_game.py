import random

# Function to run the game
def guess_the_number_game():
    # Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)

    # Prompt the user for their guess
    guess = int(input("Guess the secret number between 1 and 10: "))

    # Match the guess with the secret number
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

# Main loop to ask the user if they want to play again
def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        guess_the_number_game()
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    main()
