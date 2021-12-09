# PSP Assignment 3
# Location: AllPaws Cat Shelter
# Last modified: December 7, 2021
# Created by Vince Ruel Alonte
# The inputs for this location is STRICLY Y or N only. Inputing other characters or numbers results in a wrong choice.
# PurrPoints, Lives, CatList, Username will be grabed from the Master Python File and used as running variables this location

#A Function that will create a list from the users input on what actions they prefer.
def userinput():
    print()
    ibrush = str(input("    Brush Me (Y/N): "))
    ipet = str(input("    Pet Me (Y/N): "))
    iother = str(input("    Have you already adopted another cat (Y/N): "))
    iplay = str(input("    Play with Me (Y/N): "))
    itreat = str(input("    Give Treat (Y/N): "))
    inputlist = [ibrush,ipet,iother,iplay,itreat]
    return inputlist

# A function that calculate the amount of points by comparing the users list to the correct list
# Each correct comparison equals a point
# Only for Loki
def lokipoints(illist):
    lokicombination = ("Y", "Y", "Y", "Y", "N") # Correct Combination of Inputs for Loki
    lokipoints = 0
    for trait in range(5):
        if lokicombination[trait] == illist[trait].upper():
            lokipoints += 1
    return lokipoints

# A function that calculate the amount of points by comparing the users list to the correct list
# Each correct comparison equals a point
# Only for Boo
def boopoints(iblist):
    boocombination = ("Y", "Y", "Y", "Y", "Y") # Correct Combination of Inputs for Boo
    boopoints = 0
    for trait in range(5):
        if boocombination[trait] == iblist[trait].upper():
            boopoints += 1
    return boopoints

# A function that calculate the amount of points by comparing the users list to the correct list
# Each correct comparison equals a point
# Only for Wanda
def wandapoints(iwlist):
    wandacombination = ("N", "Y", "Y", "N", "N") # Correct Combination of Inputs for Wanda
    wandapoints = 0
    for trait in range(5):
        if wandacombination[trait] == iwlist[trait].upper():
            wandapoints += 1
    return wandapoints

# A function that calculate the amount of points by comparing the users list to the correct list
# Each correct comparison equals a point
# Only for Tobi
def tobipoints(itlist):
    tobicombination = ("N", "Y", "Y", "Y", "Y") # Correct Combination of Inputs for Tobi
    tobipoints = 0
    for trait in range(5):
        if tobicombination[trait] == itlist[trait].upper():
            tobipoints += 1
    return tobipoints

# A function that would translate the amount points it A generic output.
def pointstranslate(points):
    response = "This Should be Overwritten"
    if points == 5:
        response = "CONGRATULATIONS! We are going home together Pur-riend"
    elif points == 4:
        response = "Give me a sec to think about it!"
    elif points == 3:
        response = "I'm still deciding. But If I go with you, you have to be a better Owner! Meow!"
    else:
        response = "I don't wanna go with you! We are just too different!"
    return response

# A function that would calculate the probabilty to adopt the cat.
# If the user has collected 4 purrpoints for the current cat, the probability of adoption is 80%
# If the user has collected 3 purrpoints for the current cat, the probability of apoption is 60%
# 5 purrpoints is automatic adoption
# 0,1,2 purrpoints is No adpotion
def adoptcat(points):
    import random
    adopt = 99999 # should be over written to 0 or 1. Zero NO ADOPT. One ADOPT
    if points == 5:
        adopt = 1
    elif points == 4:
        chance = random.randint(1,10)
        if chance <= 2:
            adopt = 0
        else:
            adopt = 1
    elif points == 3:
        chance = random.randint(1,10)
        if chance <= 4:
            adopt = 0
        else:
            adopt = 1
    else:
        adopt = 0
    return adopt


#This is the function will use the Master userstate dictionary to check the current lives, name, purrpoints and catlist
def main(fpurrpoints,adoptedcatlist,name,flives):
    import random
    purrpoints = fpurrpoints
    lives = flives
    # Introduction to the Location
    # Additional Instruction for the player for the location quirk
    print("Welcome, " + name + " to AllPaws Cat Shelter") #Add User/Player Name
    print("Here you'll have the posibility to meet 4 new different Cats")
    print()
    print("NOTE: Each location has their own quirk!!!!")
    print("AllPaws Cat Shelter still gives you PurrPoints even if the cat does not want to be adopted") #Ask the team if this is okay. Easy fix
    print("This Shelter always asks you 5 questions for each cat. Every correct answer earns you 1 PurrPoint.")
    print()
    print("REMEMBER: Every cat that chooses not to be adopted you lose a life!")
    print()
    print("You " + name + " currently you have " + str(lives) + " life points left")
    print("Get ready to meet our cats!")
    print()


#Cats available for this location
#I will get randomized so the cats are not served in order
    loc4catlist = ["loki", "boo", "wanda", "tobi"]
    random.shuffle(loc4catlist)

#For the shuffled list each cat will be called.
#An intro text will be given for the user to read.
#From there the person will choose the actions that will please the cat.
#the first function that is called is the userinput function
#the next is the "catname"point function to calculate the amount of purrpoints earned
#the amount of purrpoints is added to the total purrpoints
#next the pointtranslate file is called to print a generic statement
#finally the chance to adpot the cat is calculated
#a value of 1 means the cat will be adopted (Appended to the List)
#while a value of 0 means that the user recieve a -1 from their life and not adopted
    print()
    for cats in loc4catlist:
        if cats == "loki":
            print()
            print("Meow, I’m Loki, I’m a beautiful Ragdoll Cat. I like warm places, and lounging in my favorite snuggly blanket. Paw-don me if I’m a little bit hiss-terical with kids, I’m just a little old now but I’m fiercely loyal kinda like a dog, but better because dogs are in-furior to cats. Duh!")
            lokiinput = userinput()
            print()
            print("The number of PurrPoints you got from Loki is: ", lokipoints(lokiinput))
            purrpoints += lokipoints(lokiinput) 
            print()
            print(pointstranslate(lokipoints(lokiinput)))
            lokiadopt = adoptcat(lokipoints(lokiinput))
            if lokiadopt == 1:
                adoptedcatlist.append(cats) 
                print("Loki, has chosen to be Adopted and Become Friends FURever")
            elif lokiadopt == 0:
                print(
                """Hello, LOKI here! I DON'T like you! Meow!
                 |\___/|
                 )     (
                =\     /=
                  )===(
                 (     )
                 |     |
                (       )      
                \       /
                 \__  _/
                   ( (
                    ) )
                   (_(
                """)
                print("Sorry have lost a life")
                lives -= 1
                if lives == 0:
                    break
            print()
            


        elif cats == "boo":
            print()
            print("Meow, I’m Boo! I’m a Persian kitten, please whisker me away to places because I love exploring! When I grow up, I want to join the olympics, because I’m cathletic! I love everyone including the UPS guy who brings me treats sometimes. I’m sure you’re going to love me meow until fur-ever!")
            booinput = userinput()
            print()
            print("The number of PurrPoints you got from Boo is: ", boopoints(booinput))
            purrpoints += boopoints(booinput)  
            print()
            print(pointstranslate(boopoints(booinput)))
            booadopt = adoptcat(boopoints(booinput))
            if booadopt == 1:
                adoptedcatlist.append(cats) 
                print("BOO, has chosen to be Adopted and Become Friends FURever")
            elif booadopt == 0:
                print(
                """Hello, BOO here! I DON'T like you! Meow!
                 |\___/|
                 )     (
                =\     /=
                  )===(
                 (     )
                 |     |
                (       )      
                \       /
                 \__  _/
                   ( (
                    ) )
                   (_(
                """)
                lives -= 1
                if lives == 0:
                    break
            print()



        elif cats == "wanda":
            print()
            print("Meow, are you feline good? I’m Wanda,and I love people. I dream of becoming the UN ambassador for Cat-nada! Snuggling is my number one priority! If only people were half as friendly as me, then the world would be paw-some.")
            wandainput = userinput()
            print()
            print("The number of PurrPoints you got from Wanda is: ", wandapoints(wandainput))
            purrpoints += wandapoints(wandainput)
            print()
            print(pointstranslate(wandapoints(wandainput)))
            wandaadopt = adoptcat(wandapoints(wandainput))
            if wandaadopt == 1:
                adoptedcatlist.append(cats)  
                print("WANDA, has chosen to be Adopted and Become Friends FURever")
            elif wandaadopt == 0:
                print(
                """Hello, WANDA here! I DON'T like you! Meow!
                 |\___/|
                 )     (
                =\     /=
                  )===(
                 (     )
                 |     |
                (       )      
                \       /
                 \__  _/
                   ( (
                    ) )
                   (_(
                """)
                lives -= 1
                if lives == 0:
                    break
            print()


        
        else:
            print()
            print("Meow, I’m Tobi! I’m a Burmese Cat. If I brush against you, that’s code for “Snuggles paw-lease”. Call the claw-enforcement because I will follow you all day, sit next to you, and brush against you!! What can I say? I just love you meowst.")
            tobiinput = userinput()
            print()
            print("The number of PurrPoints you got from Tobi is: ", tobipoints(tobiinput))
            purrpoints += tobipoints(tobiinput)
            print()
            print(pointstranslate(tobipoints(tobiinput)))
            tobiadopt = adoptcat(tobipoints(tobiinput))
            if tobiadopt == 1:
                adoptedcatlist.append(cats) 
                print("TOBI, has chosen to be Adopted and Become Friends FURever")
            elif tobiadopt == 0:
                print(
                """Hello, TOBI here! I DON'T like you! Meow!
                 |\___/|
                 )     (
                =\     /=
                  )===(
                 (     )
                 |     |
                (       )      
                \       /
                 \__  _/
                   ( (
                    ) )
                   (_(
                """)
                lives -= 1
                if lives == 0:
                    break
            print()
    return (purrpoints,lives)
    #the main function returns a tuple that will be used to update the dictionaty with the current purrpoints and lives


if __name__=='__main__':

    userstate = {'points':0, 'cats_collected':[], 'username':'Pecus', 'lives':1 }
    main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives'])

    # if userstate['lives']==0:
    #     print ("GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! ")
    #     print ("Here is you game summary: ")
    #     print (userstate)