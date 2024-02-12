import random

user = 0
computer = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("You won")
        user += 1
        
    elif user_input == paper and computer_guess == "rock":
        print("You Won")
        user += 1

    elif user_input == scissors and computer_guess == "paper":
        print("Yoy won")
        user += 1

    else:
        print("You lost")
        computer += 1

print("You won", user, "times")
print("Computer won", computer, "times")
print("Thanks for playing")