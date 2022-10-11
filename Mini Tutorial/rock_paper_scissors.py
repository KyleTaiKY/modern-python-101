#inport random for random function
import random

#define a function
def get_choices():
  #get user input
  player_choice = input("Enter a choice (rock, paper, scissors): ")

  options = ["paper", "scissors", "rock"]
  computer_choice = random.choice(options)
  #define a dictionary
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  #print("You chose " + player + ", computer chose " + computer)
  #print f string
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!" 
  elif player == "rock":
    if computer == "scissors":
      return "You win."
    else:
      return "You lose."
  elif player == "scissors":
    if computer == "stone":
      return "You lose."
    else:
      return "You win"
  elif player == "paper":
    if computer == "scissors":
      return "You lose."
    else:
      return "You win."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)