ch=input("Welcome!! Are you ready to play Rock, Paper, Scissors?!! Please enter Yes or No:")
import random
while ch.lower()=="y" or ch.lower()=="yes":
    moves=["ROCK","PAPER","SCISSORS"]
def play():
    ch = input("Welcome!! Are you ready to play Rock, Paper, Scissors? Please enter Yes or No: ").strip().lower()

    while ch in ("y", "yes"):
        moves = ["rock", "paper", "scissors"]
        computer = random.choice(moves)
        player = input("Enter your move: Rock, Paper or Scissors: ").strip().lower()

        print(f"You chose: {player.title()} while the computer chose: {computer.title()}")

        if player not in moves:
            print("Wrong input! Please check your spelling and choose Rock, Paper or Scissors.")
        else:
            if computer == player:
                print("It's a tie! Please replay")
            elif computer == "rock":
                if player == "paper":
                    print("You got the point!! Paper covers Rock!! YAY!!")
                else:  # player == "scissors"
                    print("The computer got a point! Rock smashes Scissors! Ouch!!")
            elif computer == "paper":
                if player == "scissors":
                    print("You got the point!! Scissors cuts Paper!! YAY!!")
                else:  # player == "rock"
                    print("The computer got a point! Paper covers Rock! Ouch!!")
            elif computer == "scissors":
                if player == "rock":
                    print("You got the point!! Rock smashes Scissors!! YAY!!")
                else:  # player == "paper"
                    print("The computer got a point! Scissors cuts Paper! Ouch!!")

        ch = input("Do you want to play for more points? Enter Yes or No: ").strip().lower()

    print("Thank you for playing the game! Hope you enjoyed it!")


if __name__ == "__main__":
    play()