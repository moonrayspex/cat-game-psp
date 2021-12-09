## Kendyll's Location Code ##
## Kitten City Rescue: Yams, Leaf, Fox, Dana ##
## Followed Vince's code ##
## Changed Vince's Location and Cat contents ##
## Changed: game print statements (location intro, ascii cats, positive/negative reaction from cat)
## Changed: variable and function names (cat names, cat points, cat input, cat lists, cat lives, cat trait combination)
## Karen Whillans, GEOM67, Fall 2021 ##
## Assignment 2, Implementation ##
## Kendyll Jones-McGowan, Section 61 ##

## define user action inputs ##

def userinput():
        print()
        ibrush = str(input(" Would you like to Brush Me? (Y/N): "))
        ipet = str(input(" Would you like to Pet Me? (Y/N): "))
        iother = str(input(" Have you already adopted another cat? (Y/N): "))
        iplay = str(input(" Would you like to play with Me? (Y/N): "))
        itreat = str(input(" Would you like to give me a treat? (Y/N): "))
        inputlist = [ibrush,ipet,iother,iplay,itreat]
        return inputlist

## define cat traits and purrpoints ##

def yamspoints(iylist):
        yamscombination = ("N","Y","Y","Y","Y")
        yamspoints = 0
        for trait in range(5):
                if yamscombination[trait] == iylist[trait].upper():
                        yamspoints += 1
        return yamspoints

def leafpoints(illist):
        leafcombination = ("Y","N","N","N","Y")
        leafpoints = 0
        for trait in range(5):
                if leafcombination[trait] == illist[trait].upper():
                        leafpoints += 1
        return leafpoints

def foxpoints(iflist):
        foxcombination = ("N","Y","Y","Y","Y")
        foxpoints = 0
        for trait in range(5):
                if foxcombination[trait] == iflist[trait].upper():
                        foxpoints += 1
        return foxpoints

def danapoints(idlist):
        danacombination = ("Y","Y","N","N","N")
        danapoints = 0
        for trait in range(5):
                if danacombination[trait] == idlist[trait].upper():
                        danapoints += 1
        return danapoints

## purrpoint print statements ##

def pointstranslate(points):
        response = "should be overwritten"
        if points == 5:
                response = "CON-CAT-ULATIONS! We are going home together Fuuuriend"
        elif points == 4:
                response = "Purrr... Give me a sec To think about it..."
        elif points == 3:
                response = "I'm still deciding... But If I go with you, you have to be a better Owner! Meow!"
        else:
                response = "I don't want to go home with you. HISS!"
        return response

## adoption chance based on purrpoints ##

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

## refers to main function in Master ##

def main(mainpoints,maincatlist,username,livesleft):
        import random
        #userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives': 2}
        name = username
        purrpoints = mainpoints
        adoptedcatlist = maincatlist
        lives = livesleft

## Introduction to the Location ##

        print()
        print("***************************************************************************************************************************************")
        print("Meow-come to Kitten City Rescue! We have so many purrrfect cats here, and all of them can't wait to meet you!")
        print("We hope you have a blast getting to know each of our paw-some friends! Enjoy," + name + "... and stay as long as you would like!")
        print()
        print("Here you'll get to meet 4 new Cats! Try to adopt them all by choosing the right interactions to befriend them")
        print()
        print("NOTE: Each location has it's own quirk!")
        print()
        print("Here at Kitten City Rescue we always ask you 5 questions for each cat. Every correct answer earns you 1 PurrPoint!")
        print()
        print("REMEMBER: You will lose 1 life per Cat that doesn't want to be adopted by you!")
        print()
        print(name + " currently you have " + str(lives) + " life points left")
        print()
        print("We hope you enjoy meeting our cats! Good luck!")
        print("***************************************************************************************************************************************")        
        print()

## list cats at Kitten City Rescue location, randomly shuffle them ##

        loc2catlist = ["yams", "leaf", "fox", "dana"]
        random.shuffle(loc2catlist)

## begin Kitten City Rescue cat interaction gameplay ##

        print()
        for cats in loc2catlist:
                if cats == "yams":
                        print("***************************************************************************************************************************************")
                        print("Meow, my name is Yams! I am an orange Short-Hair kitten with lots of energy. Lets go on an adventure outside and get lost! It is so much fun to sneak out of the house. I love pets, other cats, playing and yummy treats...")
                        yamsinput = userinput()
                        print(yamsinput)
                        print()
                        print("The number of PurrPoints you got from Yams is: ", yamspoints(yamsinput))
                        purrpoints += yamspoints(yamsinput)
                        print()
                        print(pointstranslate(yamspoints(yamsinput)))
                        yamsadopt = adoptcat(yamspoints(yamsinput))
                        if yamsadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""
                                I have decided... please adopt me!
                   _ |\_
                   \` ..|
              __,.-" =__Y=
            ."        )
      _    /   ,    \/\_
     ((____|    )_-\ \_-`
     `-----'`-----` `--`""")
                                print()
                                print("Meow! I am so excited to go home with you. Friends fuuurever! Let's go outside for a walk!") #make more puns
                        elif yamsadopt == 0:
                                print(
                        """Meow, I don't think this is going to work out...
                  _
               |\/(__
               /     \_  
               |  __==/
               /   (
              ;     |
             /      |
            /    ,  /
          .'      | |
         /      --; |
         |         ||  __
         |        /_;-` _`'.
         \  '-----' _.-` '._)
          `'-------'""")
                                print()
                                print("Sorry, I don't want you to adopt me and you have LOST 1 life")
                                lives -= 1     #change
                                if lives == 0:
                                        break
                        print()


                elif cats == "leaf":
                        print("***************************************************************************************************************************************")
                        print("Meow, my name is Leaf! I am a black Short-Hair adult cat and I like to act aloof. I am happiest when napping in the corner while you read on a cozy winter day. I don't like other cats, but I love brushing and yummy treats...")
                        leafinput = userinput()
                        print(leafinput)
                        print()
                        print("The number of PurrPoints you got from Leaf is: ", leafpoints(leafinput))
                        purrpoints += leafpoints(leafinput)     #change 
                        print()
                        print(pointstranslate(leafpoints(leafinput)))
                        print()
                        leafadopt = adoptcat(leafpoints(leafinput))
                        if leafadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""
                                I have decided... please adopt me!       
   /\_/
   >^.^<.---.
  _'-`-'     )|
 (6--\ |--\ (`.`-.
     --'  --'  ``-'""")
                                print()
                                print("Meow! I am so excited to go home with you. Friends fuuurever! I am going to nap alone in the corner now.")
                        elif leafadopt == 0:
                                print(
                        """Meow, I don't think this is going to work out...
            /|
            \ |
             \ |
             / /
            / /
           _\ \_/\/|
          /  *  \@@ =
         |       |Y/
         |       |~
          \ /_\ /
           || //
            |||
           _|||_
          ( / \ )
            """)
                                print()
                                print("Sorry, I don't want you to adopt me and you have LOST 1 life")
                                lives -= 1      #change to to use the master
                                if lives == 0:
                                        break
                        print()


                elif cats == "fox":
                        print("***************************************************************************************************************************************")
                        print("Meow, my name is Fox! I am an orange-white Short-Hair adult cat that's full of curosity. I like to stare out the window and watch birds all day. I love pets, other cats, playng and yummy treats...")
                        foxinput = userinput()
                        print(foxinput)
                        print()
                        print("The number of PurrPoints you got from Fox is: ", foxpoints(foxinput))
                        purrpoints += foxpoints(foxinput)     #change
                        print()
                        print(pointstranslate(foxpoints(foxinput)))
                        print()
                        foxadopt = adoptcat(foxpoints(foxinput))
                        if foxadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""
                                I have decided... please adopt me!   
                      ,
                    _/((
           _.---. .'   `|
         .'      `     ^ T=
        /     \       .--'
       |      /       )'-.
       ; ,   <__..-(   '-.)
        \ \-.__)    ``--._)
         '.'-.__.-.
           '-...-'  """)
                                print()
                                print()
                                print("Meow! I am so excited to go home with you. Friends fuuurever! Let's go bird watching!")
                        elif foxadopt == 0:
                                print(
                        """Meow, I don't think this is going to work out...
            |\___/|
            )     (
           =\     /=
             )===(
            /     |
            |     |
           /       |
           \       /
            \__  _/
              ( (
               ) )
              (_(
            """)
                                print()
                                print("Sorry, I don't want you to adopt me and you have LOST 1 life")
                                lives -= 1#change to to use the master
                                if lives == 0:
                                        break
                        print()



                else:
                        print("***************************************************************************************************************************************")
                        print("Meow, my name is Dana! I am a calico Short-Hair adult cat that is very independent. My perfect day includes napping while the sun is up and running around the house late at night. I don't like other cats, but I love brushing...")
                        danainput = userinput()
                        print(danainput)
                        print()
                        print("The number of PurrPoints you got from Dana is: ", danapoints(danainput))
                        purrpoints += danapoints(danainput)     #change
                        print()
                        print(pointstranslate(danapoints(danainput)))
                        print()
                        danaadopt = adoptcat(danapoints(danainput))
                        if danaadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""
                                I have decided... please adopt me!   
                 (\(|
                 / ..(
              .-' ,_Y/
            .'     (
           /   \/  |
          _|  _/| //
        .',_\__)\_))
        '----,)""")
                                print()
                                print()
                                print("Meow! I am so excited to go home with you. Friends fuuurever! Let's go nap!") #make more puns
                        elif danaadopt == 0:
                                print(
                """Meow, I don't think this is going to work out...
                              / )
              (\__/)         ( (
              )    (          ) )
            ={      }=       / /
              )     `-------/ /
             (              */
              \              |
             ,'\       ,    ,'
             `-'\  ,---\   | |
                _) )    `. \ /
               (__/       ) ) 
                         (_/""")
                                print()
                                print("Sorry, I don't want you to adopt me and you have LOST 1 life")
                                lives -= 1     #change to to use the master
                        if lives == 0:
                                break
                        print()
        print("You have earned " + str(purrpoints) + " points, and have " + str(lives) + " lives left!")
        return (purrpoints,lives)


        # extra goodbye code
#         print("""Thank you so much for coming to Kitty City Rescue! We hope you had a wonderful visit...      
#         _                        
#         \`*-.                    
#          )  _`-.                 
#         .  : `. .                
#         : _   '  \               
#         ; *` _.   `*-._          
#         `-.-'          `-.       
#           ;       `       `.     
#           :.       .        \    
#           . \  .   :   .-'   .   
#           '  `+.;  ;  '      :   
#           :  '  |    ;       ;-. 
#           ; '   : :`-:     _.`* ;
#        .*' /  .*' ; .*`- +'  `*' 
#        `*-*   `*-*  `*-*'
#         Please, come again soon! Meow!""")

## refers to main function in Master ##

if __name__ == '__main__':
        userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives': 2}
        main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives'])

#(username, points, cats_collected)
