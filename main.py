from Arena import Arena
from BattleBot import BattleBot
import time
clear_screen = "\n" * 30
divider = "_" * 30
space_large = " " * 18
space_small = " " * 9
print("\nWant to see if you can defeat your enemy? Try our lucky with the 'Knows-It-All' super machine which can predict if you would win a figth against anyone")
print("   _______________________")
print("\n  |         |\   /|        |\n  |         \|_|/          |\n  |         /. .\          | ")
print("  |        =\_Y_/=         |\n  |         {>o<}          |\n  |                        |\n  |   [Mrs. Knows-It-All]  |")
print("   _______________________\n")
time.sleep(4)
def main():
  start_game = input("Do you want to play?\n\nPress 'y' for yes and 'n' for no: ").lower()
  if start_game == "y":
    print(divider * 2)
    player1 = input("\nType your name: ").capitalize()
    player2 = input("\nType your enemy's name: ").capitalize()
    print(clear_screen)
    print("\n°°°°°°°°°°°°°°°°°°°°°°°\n¬ Starting your game ¬\n°°°°°°°°°°°°°°°°°°°°°°°\n")
    time.sleep(1.5)
    Bot1 = BattleBot(player1)
    Bot2 = BattleBot(player2)
    arena =  Arena(Bot1, Bot2)
    arena.battle()
  elif start_game == "n":
    double_check = input("\nAre you sure?\nAgain, press 'y' for yes and 'n' for no: ").lower()
    if double_check == "y":
      print(clear_screen + "- Mrs. Knows-It-All: Okay then...But come back later or you'll regret it. I will be rigth here waiting to see your lucky. ")
      time.sleep(5)
      print("\n- Mrs. Knows-It-All: See ya ;)")
      time.sleep(4)
      print("   _______________________")
      print("\n  |         |\   /|        |\n  |         \|_|/          |\n  |         /º º\          | ")
      print("  |        =\_^_/=         |\n  |         {>o<}          |\n  |                        |")
      print("   _______________________\n")
      time.sleep(5)
      quit
    elif double_check == "n":
      print("\nOkay. Let's try again then.\n")
      print(divider +"\n\n" + space_small + "Resseting...\n" + space_small + "\n" + divider)
      time.sleep(4)
      print(clear_screen)
      main ()
    else:
      print("\n" + (divider * 2) + "\n" + space_small + "Check if you're typing it correctly.\n" + (divider * 2))
      time.sleep(6)
      input("\n\nPress enter to try again")
      print(clear_screen)
      main ()
  else: 
    print("\n" + (divider * 2) + "\n" + space_small + "Check if you're typing it correctly.\n" + (divider * 2))
    time.sleep(6)
    input("\n\nPress enter to try again")
    print(clear_screen)
    main ()
main ()
                        