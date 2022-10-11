"""
Guess planet game
"""

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# Alternative 1
while correct_guess is not True:
  guess = input("Can you guess my planet? >>> ")
  if guess.lower() == planet.lower():
    correct_guess = True
    print("Right guess!")
  else:
    print("Wrong guess!")



# Alternative 2
while True:
  guess = input("Can you guess my planet? >>> ")
  if guess.lower() == planet.lower():
    print("Right guess!")
    break
  else:
    print("Wrong guess!")

  