## Group 2, Project 2
## GEOM 67, Problem Solving and Programming, Karen Whillans
## Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte
## Last Modified: December 7th, 2021

## Find the Purrrrfect Friend Game

## Welcome to Find the Purrrrfect Friend Game!

## With the increase of individuals wanting to get cats as pets, we wanted to create an educational game that will inform players...  
## ... (aka Potential  Cat  Owners/Current  Cat  Owners) of the  different  personalities  of common cat breeds. The game will be limited to... 
## ...16 unique cat profiles. This text-based game is a one-player game. 

## The player is presented with different cat profiles at four unique locations, and selects how they would like to interact with each cat...
## ...The player can adopt a cat if they choose the right actions based on each cats personality... 
## ...The player will be awarded PurrPoints for each correct action chosen (but remember: each location has it's own quirk with regards to adoption chance and purrPoints!)...
## ... If the player selects enough correct actions, they will have a random chance of being able to adopt the cat!...
## ... if the player is unsuccessful in adopting the cat, they will lose 1 of their 9 lives!

## Have fun and enjoy Group 2's hard work! =^..^=


# import these two modules for later functions
import math
import random
# import all .py files that have each main() function for each location
import Rachel
import Vince
import Kendyll
import Carol

# Display program purpose
#defining print_intro as a funtion
def print_intro():
    print('=^..^=     ','=^..^=     ','=^..^=     ' )
    print('      =^..^=     ','=^..^=     ')
    print("Welcome to 'PURRfect Pals'")
    print()
    print(' =^..^= ')
    print("Get ready to meet and adopt feline friends from four different cat rescues.")
    print("Each cat is looking for their furrever home, will you be the purrfect match?")
    print()
    print("The Goal of the game is to adopt all 16 cats!")
    print("And to collect as many PurrPoints as possible!")
    print("You have 9 lives!!")
    print("Note: Be sure to read the instruction for each location as there may be some quirks!!")

#defining the main program function
def main():
    #random.shuffle returns the list in a random order
    location = ["LRachel", "LVince", "LKendyll", "LCarol"]
    random.shuffle(location)

    #user state to retain and hold accrued points and cats
    #dictionary to get passed around location files and hold the state of the game
    userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives':9 }

    #call in print_intro
    print_intro()

    #get the user's name
    print()
    userstate['username'] = str(input("   Gamer, what is your name? "))
    print()

    #for loop to iterate through each location
    for loc in location:
        if loc == "LRachel":
            userstate = Rachel.main(userstate)
            if userstate['lives'] == 0:
                break
        elif loc == "LKendyll":
            kendylltuple=(Kendyll.main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives']))
            userstate['points'] = kendylltuple[0]
            userstate['lives'] = kendylltuple[1]
            if userstate['lives'] == 0:
                break
        elif loc == "LCarol":
            caroltuple = Carol.main(userstate)
            print(caroltuple)
            # had to change keys to points/lives vs 0/1 as they were in default program layout
            userstate['points'] = caroltuple['points']
            userstate['lives'] = caroltuple['lives']
            if userstate['lives'] == 0:
                break
        else:
            vincetuple = Vince.main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives'])
            print(vincetuple)
            userstate['points'] = vincetuple[0] #updates the current number of purrpoint
            userstate['lives'] = vincetuple[1] #update the current number of lives
            if userstate['lives'] == 0:
                break

    if userstate['lives'] == 0:
        print()
        print ("GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! ")
        print ("Here is your game summary: ")
        print ("    You adopted these cats:")
        print ("        " + str(userstate["cats_collected"]))
        print ("    Your total PurrPoints collected is " + str(userstate["points"]))
    else:
        print()
        print ("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMEOW!!!!!!")
        print ("Congratulations for Finishing the the game!")
        print ("Here is your game summary: ")
        print ("    You adopted these cats:")
        print ("        " + str(userstate["cats_collected"]))
        print ("    Your total PurrPoints collected is " + str(userstate["points"]))
        print ("    Lives Left: " + str(userstate["lives"]))
        print("""
         *                  *
             __                *
          ,db'    *     *
         ,d8/       *        *    *
         888
         `db\       *     *
           `o`_                    **
      *               *   *    _      *
            *                 / )
         *    (\__/) *       ( (  *
       ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
      | @|  ={      }= | @|  / / | @|o |
     _j__j__j_)     `-------/ /__j__j__j_
     ________(               /___________
      |  | @| \              || o|O | @|
      |o |  |,'\       ,   ,'"|  |  |  |  hjw
     vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
                _) )    `. \ /
               (__/       ) )
                         (_/
""")

if __name__=='__main__':  #calling defined function 'main'
    main()
