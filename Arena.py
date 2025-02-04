import time
clear_screen = "\n" * 30
divider = "_" * 30
space_small = " " * 9
class Arena:
    def __init__(self, Bot1, Bot2):
        self.bbot1 = Bot1
        self.bbot2 = Bot2
    def battle(self):
        number_rounds = 0
        while number_rounds >= 0:
          while self.bbot1.is_alive() and self.bbot2.is_alive():
                number_rounds += 1
                print("* STATUS UPDATE *\n")
                if self.bbot1.speed <= self.bbot2.speed:
                    self.bbot1.action(self.bbot2)
                    self.bbot2.action(self.bbot1)
                    self.bbot1.get_stats()
                    self.bbot2.get_stats()
                    print("- Get ready for " + str((number_rounds + 1)) + " round!! -\n")
                    print(divider)
                    input("\nPress enter to go to the next round\n" + divider)
                    time.sleep(1)
                    print(clear_screen)
                else:
                    self.bbot2.action(self.bbot1)
                    self.bbot1.action(self.bbot2)
                    self.bbot1.get_stats()
                    self.bbot2.get_stats()
                    print("- Get ready for " + str((number_rounds + 1)) + " round!! -\n")
                    print(divider)
                    input("\nPress enter to go to the next round\n" + divider)
                    time.sleep(1)
                    print(clear_screen)
          if self.bbot1.is_alive():
              print(space_small + self.bbot1.name + " is the winner!")
              print("   _______________________")
              print("\n  |         |\   /|        |\n  |         \|_|/          |\n  |         /. .\          | ")
              print("  |        =\_0_/=         |\n  |         {>o<}          |\n  |                        |\n  |                        |")
              print("   _______________________\n")
              print("Mrs. Knows-It-All: Great job kid! Now you know that you are totally able to defeat all of your enemies.")
              break
          else:
              print(self.bbot2.name + " is the winner!")
              print("   _______________________")
              print("\n  |         |\   /|        |\n  |         \|_|/          |\n  |         /. .\          | ")
              print("  |        =\_Q_/=         |\n  |         {>o<}          |\n  |                        |\n  |                        |")
              print("   _______________________\n")
              print("Mrs. Knows-It-All: It seems that the other one wins.")
              print("   _______________________")
              print("\n  |         |\   /|        |\n  |         \|_|/          |\n  |         /. .\          | ")
              print("  |        =\_Q_/=         |\n  |         {>o<}          |\n  |                        |\n  |                        |")
              print("   _______________________\n")
              print("Mrs. Knows-It-All: Don't be sad. You can try another one more time if you feel like it.")
              #try_again = input("Do you want to try again?")
                #if try_again == "y":
                 # print("You will be able to")
                 # main()
                #elif try_again == "n":
                #else:
                  
              break
