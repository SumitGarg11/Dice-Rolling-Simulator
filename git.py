import random

roll_again = "Y"
score=0
while roll_again =="Y":
          user = int(input("Enter Your Number: "))
          print("\nRolling the dice...")


          dice=random.randint(1,6)


          print("The values are:")
          print("User =",user,"\nDice =",dice)

          if dice == user:
              print("You Win")
              score=score+1
              print("Score =",score)
          else:
              print("Keep Trying")
          roll_again = input("\nRoll the dice again? (Y/N) ")