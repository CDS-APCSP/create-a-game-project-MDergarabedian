import os, time

health = 10
gun = False
crowbar = False
cash = 0
police = False

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome to Miami florida, You are playing GTA 6 in the year 2050,")
  print()
  print()
  print("Let's get you used to the way the city works")
  time.sleep(5) # wait 3 seconds before moving on
  crime1() # runs to send the player to crime #1

def crime1():
  global crowbar # use the gun variable from the top
  os.system('clear')
  if crowbar:
    print("You are in the first mission, you have to break into and steal a car you can choose the Red Ferrari on your left, or the White Buggati on your right. Say right to go to the Red Ferrari, left to go to the Buggati")
  else:
    print("You are in the first mission. There is a crowbar on the ground you can either take it, or leave it. Say crowbar to pick it up")
  decision = input(">>").strip().lower()
  if decision.find("crowbar") > -1:
    print("Equipping the crowbar.")
    crowbar = True
    time.sleep(3)
    crime1()
  elif decision.find("left") > -1:
    print("You broke the window and tried to hotwire the Ferrari but it did not work")
    time.sleep(3)
    crime1()
  elif decision.find("right") > -1:
    print("You broke the window with your melee and you are able to hotwire and start up the Bugatti ")
    time.sleep(3)
    crime2()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    crime1()
  

def crime2():
  global gun, health, police, cash, crowbar, gunpoint, kill
  os.system('clear')
  print("Welcome to your next mission, you have to rob a store and successfully get away in your new car")
  if gun:
   print ("You have pulled up to the store, and you are armed with a handgun, now you can either hold the clerk at gunpoint until you get the cash from the register, or kill the clerk and get the cash yourself. Say gunpoint or kill") 
  else:
   print ("There is a gun in the dash of the car you stole, you can either equip that to rob the store, or you can use the crowbar. Say gun to equip the gun and crowbar to equip the crowbar")
  decision = input(">>").strip().lower()
  if decision.find("gun") > -1:
    print ("Equipping the gun")
    gun = True
  elif decision.find("crowbar") > -1:
    print ("You tried to rob the store using a crowbar, however the clerk had a gun under the counter, try again") 
  else:
    print ("Sorry, that command is not found.")
    time.sleep(3)
    crime2()

    

  

def crime3():
  global health, police, gun, cash
  os.system('clear')
  pass
  if gun:
   print ("You have pulled up to the store, and you are armed with a handgun, now you can either hold the clerk at gunpoint until you get the cash from the register, or kill the clerk and get the cash yourself") 
  decision = input(">>").strip().lower()
  if decision.find("Gunpoint") > -1:
    print("You held the clerk at gunpoint, he was intimidated and handed over some cash")
    cash = 250
  elif decision.find("kill") > -1:
    print ("You killed the clerk, and could not figure out how to open the register, try again")

def crime4():
  global health, police, gun, cash
  os.system('clear')
  pass 
  if police:
    print("You have been caught by the police, game over")
  else:
    print ("You got the cash and are headed to your buggatti, you win")
def endGame():
  os.system("clear")
  pass

startGame()