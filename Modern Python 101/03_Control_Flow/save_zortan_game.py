"""
Zortan is under attack by Thanos, 4 avengers come to save Zortan

Avengers can attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we lose the game.

"""

# import final for constant int
from typing import Final

# declar our constants
IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life = 1500
choices = 0
attack_num = 0

WIN_MSG = "Congrats, you win!"
LOSE_MSG = "Game Over!"

while True:
  choice = int(input("Enter your pair no >>> "))
  if thanos_life <= 0 and attack_num < 3:
    print(WIN_MSG)
    break
  elif attack_num >= 3:
    print(LOSE_MSG)
    break

  if choice == 1:
    print("Ironman & Black Widow are attacking Thanos...")
    thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
  elif choice == 2:
    print("Black Widow & Spiderman are attacking Thanos...")
    thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
  elif choice == 3:
    print("Spiderman & Hulk are attacking Thanos...")
    thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
  elif choice == 4:
    print("Hulk & Ironman are attacking Thanos...")
    thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER

  attack_num = attack_num + 1
      
  