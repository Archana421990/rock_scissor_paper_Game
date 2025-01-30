import random

def play_game():
    player = input("Enter your choice either rock,scissor or paper : ").lower()
    AI = random.choice(["rock","scissor","paper"]).lower()
    print(f"\n you chose {player} and AI chose {AI} \n")
     
    while True:   
        if player == AI:
            print("Its a Tie break") 
        elif player == "rock":
            if AI == "scissor":
                print("Rock breaks scissor,so You are the winner in this round")
            else:
                print("Paper covers rock, so you lose the game")
        elif player == "scissor":
            if AI == "paper":
                print("scissor cuts the paper, you are the winner in this round")
            else:
                print("rock breaks scissor, so you lose the game")
        elif player == "paper":
            if AI == "rock":
                print("Paper covers rock, so you are the winner in this round")
            else:
                print("scissor cuts the paper, so you lose the game")
        else:
            print("invalid statement")
        play_again = input("Want to play? [y/n]: ")
        if play_again == "y":
            play_game() 
        else:
            quit()       
if __name__ == "__main__":
   play_game() 