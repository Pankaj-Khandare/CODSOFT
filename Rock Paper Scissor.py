import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"


def play_round():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose 'rock', 'paper', or 'scissors'.")
    
    
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice: ").lower()

    
    computer_choice = random.choice(["rock", "paper", "scissors"])

    
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result


def play_game():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        result = play_round()
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")

        
        play_again = input("Do you want to play again? (yes/no): ").lower()

    print("Thanks for playing!")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")


if __name__ == "__main__":
    play_game()

