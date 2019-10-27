#  bnc.py

# Import the random library
from random import randint

# Make an array
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

player = False

while player == False:
    #Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role
    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", player, "is shot by", computer)
        else: # computer is Cowboy, player is Ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
        else: # computer is bear, player is ninja
            print("You lose!", player, "is eaten by", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeated by", computer)
        else: # computer is ninja, player is bear
            print("You win!", player, "eats", computer)
    player = False
    computer = roles[randint(0,2)]

    # after checking who won, put the following code
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break
