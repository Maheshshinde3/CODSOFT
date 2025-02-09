import random

def get_computer_choice():
    # List of possible choices for the computer
    choices = ["rock", "paper", "scissors"]
    # Randomly choose from the list
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the rules of Rock-Paper-Scissors
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_round():
    # Prompt user for their choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Get computer's random choice
    computer_choice = get_computer_choice()
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display the result
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    print(result)

    return result

def main():
    # Initialize the scores for the user and the computer
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("You can type 'rock', 'paper', or 'scissors' to make a choice.")
    
    # Loop to play multiple rounds
    while True:
        result = play_round()
        
        # Update the scores based on the result of the round
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display the current score after each round
        print(f"\nScore: You - {user_score}, Computer - {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break

# Call the main function to start the game
if __name__ == "__main__":
    main()
