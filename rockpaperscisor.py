import random

users_wins = 0
computers_wins = 0
draw = 0
options = ["rock", "paper", "scissors"]

while True:
    users_input = input("Type rock/paper/scissors or Q to quit.").lower()
    if users_input == "q":
        break

    if users_input not in options:
        print("it is not correct!")
        continue

    random_number = random.randint(0, 2)
    # rock-0, paper-1, scissors-2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if users_input == "rock" and computer_pick == "scissors":
        print("You won!")
        users_wins += 1
        continue

    if users_input == "paper" and computer_pick == "rock":
        print("You won!")
        users_wins += 1

    elif users_input == "scissior" and computer_pick == "paper":
        print("You won!")
        users_wins += 1
        continue
    if users_input == computer_pick:
        print("This is a draw!")
        draw += 1
        continue
    else:
        print("You lost!")
        computers_wins += 1

print("You won", users_wins, "times.")
print("The computer won", computers_wins, "times.")
print("The draw was", draw, "times.")
