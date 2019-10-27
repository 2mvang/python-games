# flashcards.py

# import the json module from python3
import json

# open the file and parse the json
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

while score == 0:
    score = 0

    for i in data["cards"]:
        guess = input(i["q"] + " > ")
    # print(guess)

        if guess.lower() == i['a'].lower():
            # increment score up one
            score += 1
            # interpolate score and total into the response
            print(f"Correct! Current score: {score}/{total}")
        else:
            print("Incorrect! The correct answer was", i["a"])
            print(f"Current score: {score}/{total}")

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      score = 0
      total = len(data["cards"])
    else:
      break
