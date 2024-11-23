import os
import time
import sys

def main():
  os.system("clear")
  try:
    print("Hello.")
    time.sleep(0.5)
    print("Welcome to Battleship")
    time.sleep(1)
    while True:
       os.system("clear")
       enter=input("Type \"start\" and enter to START or \"help\" to learn more about the game\n")
       if enter=="start":
          os.system("clear")
          break
       elif enter=="help":
         while True:
          os.system("clear")
          print("Played  with 2 players.\nIn this fascinating game the players choose level, which is the size of the board to place their ships")
          time.sleep(1)
          print("And then the number of ships they wish to place")
          time.sleep(1)
          print("Then one by one they place their ships in the coordinates of their choice, varying from 0 to level-1")
          time.sleep(1)
          print("Then, one by one they try to guess where the opponent has placed his ships")
          time.sleep(1)
          print("The first one to bomb the opponents ships wins")
          time.sleep(3)
          rtrn=input("If you wish to return to main menu type \"return\" and hit enter(or anything else to review the information)\n")
          if rtrn=="return":
             break
    while True:
     try:
       level=int(input("Choose difficulty level (how big you want the sea from 3 to 10):\n"))
       if level>10 or level<3:
           raise ValueError
       else:
          break
     except ValueError:
        print("Chooce a level from 3 to 10")
       # time.sleep(1)
        os.system("clear")
        continue
    while True:
     try:
       ships=int(input("Choose number of ships (between 3 to 7)\n"))
       if ships<3 or ships>7:
          raise ValueError
       else:
          break
     except ValueError:
        print("Please between 3 to 7 ships\n")
        #time.sleep(2)
        os.system("clear")
        continue
    player1=input("What's your name, player 1?  ")
    player2=input("What's your name, player 2?  ")
    sea1=create_sea(level)
    sea2=create_sea(level)
    os.system("clear")
    time.sleep(0.5)
    print(player1+", put your ships")
    put_ships(sea1,ships,level)
    time.sleep(2)
    os.system("clear")
    passing=input("Pass the turn to the other player?\nType \"pass\" and hit enter\n")
    while pass_turn(passing)!=True:
       os.system("clear")
       passing=input("Pass the turn to the other player?\nType \"pass\" and hit enter\n")
       pass_turn(passing)
    os.system("clear")
    print(player2+" , put your ships")
    put_ships(sea2,ships,level)
    os.system("clear")
    mystery1=create_mystery(level)
    mystery2=create_mystery(level)
    hits1=0
    hits2=0
    while True:
       print(player1+". This is your ship placement: ")
       print_array(sea1,level)
       time.sleep(2)
       os.system("clear")
       print(player1+" attacks")
       if attack(sea2,mystery2,level)==True:
          hits1+=1
       if hits1==ships:
          break
       passing=input("Pass the turn to the other player?\nType \"pass\" and hit enter\n")
       while pass_turn(passing)!=True:
         os.system("clear")
         passing=input("Pass the turn to the other player?\nType \"pass\" and hit enter\n")
         pass_turn(passing)
       time.sleep(4)
       os.system("clear")
       print(player2+".This is your ship placement: ")
       print_array(sea2,level)
       time.sleep(2)
       os.system("clear")
       print(player2+" attacks")
       if attack(sea1,mystery1,level)==True:
          hits2+=1
       if hits2==ships:
          break
       passing=input("Pass the turn to the other player?\nType \"pass\" and hit enter\n")
       while pass_turn(passing)!=True:
         os.system("clear")
         passing=input("Pass the turn to the other player?\nType \"pass\" and hit enter\n")
         pass_turn(passing)
         time.sleep(4)
       os.system("clear")
    if hits1==ships:
       print(player1+" won it all")
       file = open("HallOfFame.txt", "a")
       file.write(player1+"\n")
       file.close()
    elif hits2==ships:
       print(player2+" won it all")
       file = open("HallOfFame.txt", "a")
       file.write(player2+"\n")
       file.close()
    print("Thanks for playing")
  except EOFError:
     sys.exit("Shutting Down... See you next time")



def create_sea(level):
  array = [["🌊"] * level for _ in range(level)]   #one function using a second argument as the emoji
  return array


def print_array(matrix,level):
   for i in range(0,level):
      for j in range(0,level):
         print(matrix[i][j],end="  ")
      print()

def put_ships(sea,ships,level):
   while ships>0:
    try:
      row=int(input("Choose the row to put your ship in ("+str(ships)+" ships remaining)\n"))
      col=int(input("Choose the column to put your ship in ("+str(ships)+" ships remaining)\n"))
      if sea[row][col]=="🚢":
         print("Already a ship there")
         print_array(sea,level)
         continue
      else:
        sea[row][col]="🚢"
        print_array(sea,level)
      ships-=1
    except  IndexError:
       print("Out of bounds")
       continue
    except ValueError:
       print("Incorrect input")
       continue

def create_mystery(level):
   array = [["❓"] * level for _ in range(level)]
   return array

def attack(sea,mystery,level):
   flag=False
   while True:
      try:
        row=int(input("Choose row to attack \n"))
        time.sleep(0.1)
        col=int(input("Choose col to attack\n"))
        time.sleep(0.1)
        if mystery[row][col]!="❓":
           print("Already tried that one")
           continue
        if sea[row][col]=="🚢":
          sea[row][col]="🔥"
          mystery[row][col]="🔥"
          flag=True
        else:
           mystery[row][col]="🌊"
           flag=False
        print_array(mystery,level)
        time.sleep(3)
        os.system("clear")
        return flag
        break
      except IndexError:
         print("Out of bounds")
         continue
      except ValueError:
         print("Incorrect input.Try Again")


def pass_turn(s):
   if s!="pass":
      return False
   else:
      return True

if __name__=="__main__":
    main()
