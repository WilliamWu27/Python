from random import randint
t = ["Rock", "Paper", "Scissors"]
computadora = t[randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computadora:
        print("Tie!")
    elif player == "Rock":
        if computadora == "Paper":
            print("You lose!", computadora, "covers", player)
        else:
            print("You win!", player, "smashes", computadora)
    elif player == "Paper":
        if computadora == "Scissors":
            print("You lose!", computadora, "cut", player)
        else:
            print("You win!", player, "covers", computadora)
    elif player == "Scissors":
        if computadora == "Rock":
            print("You lose...", computadora, "smashes", player)
        else:
            print("You win!", player, "cut", computadora)
    elif player == "stop":
        player = False
    else:
        print("That's not right. Go fix it")
    player = False
    computadora = t[randint(0,2)]