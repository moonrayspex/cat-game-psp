# Carol.py test file; not a working code yet
# DESIGNED FOR:
# group 2 project 2
# GEOM 67, Problem Solving and Programming, Karen Whillans
# Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte
## Find the Purrrrfect Friend Game ##

# main definition and call at end is from RachelM

import math
import random
#define functions
# def main(username):
#     print("Hello " + username)

# list of dictionaries for cats at Happy Tails Rescue
def happy_tails_cats():
  return [
      {
        'name': 'Buster',
        'color': 'brown-black',
        'breed': "Maine Coon",
        'personality': 'annoying',
        'age': 'kitten',
        'intro': "Meeeeeeow! I'm Buster, and I'm the meowst annoying kitten you'll ever meet!! You wanna play?! Let's play all day!!",
        'actions': [
            {'actionName': 'othercats', 'likes': True},
            {'actionName': 'brushing', 'likes': True },
            {'actionName': 'pets', 'likes': True},
            {'actionName': 'playing', 'likes': True},
            {'actionName': 'treats', 'likes': True},
        ]
      },
      {
        'name': 'Ophelia',
        'color': 'black',
        'breed': "Short-Hair",
        'personality': 'aloof',
        'age': 'senior',
        'intro': "Greetings, human. My mature aloof nature sets me apart from the other cats here. ... oh, my name? Ophelia.",
        'actions': [
            {'actionName': 'othercats', 'likes': False},
            {'actionName': 'brushing', 'likes': False },
            {'actionName': 'pets', 'likes': False},
            {'actionName': 'playing', 'likes': False},
            {'actionName': 'treats', 'likes': True},
        ]
      },
      {
        'name': 'Artemis',
        'color': 'black-white',
        'breed': "Short-Hair",
        'personality': 'independent',
        'age': 'adult',
        'intro': "Hewwo, my name is Artemis. I'm an indepedent cat, and I love to spend my days sunbathing and enjoying the great outdoors.",
        'actions': [
            {'actionName': 'othercats', 'likes': False},
            {'actionName': 'brushing', 'likes': True },
            {'actionName': 'pets', 'likes': True},
            {'actionName': 'playing', 'likes': False},
            {'actionName': 'treats', 'likes': True},
        ]
      },
      {
        'name': 'Gary',
        'color': 'grey',
        'breed': "Scottish-Fold",
        'personality': 'dopey',
        'age': 'kitten',
        'intro': "Hiya, my name is Gary and I'm a dopey kitteh. I'd love to just flop down and nap in your lap for hours!",
        'actions': [
            {'actionName': 'othercats', 'likes': True},
            {'actionName': 'brushing', 'likes': False },
            {'actionName': 'pets', 'likes': True},
            {'actionName': 'playing', 'likes': True},
            {'actionName': 'treats', 'likes': True},
        ]
      },
  ]

# this function will display this message when my location comes up in the game
def welcome_message():
    print("  >^.^<   Hey y'all, and welcome to Happy Tails Rescue! Let's see if we can find some cats to be your furever friends!!  >^.^< ")
    print("""
                       (`.-,')
                     .-'     ;
                 _.-'      ,-
           _ _.-'         /._
         .' `  _.-.     ,'._;)
        (       .  )-| (
         )`,_ ,'_,'  \_;)  fL 
 ('_  _,'.'  (___,))
  `-:;.-'
     """) # credit to Felix Lee for ascii cat, slightly modified by CB
    print("Here you'll get to meet 4 new Cats! Try to adopt them all by choosing the right interactions to befriend them")
    print()
    print("Every correct answer earns you 1 PurrPoint! But REMEMBER: You will lose 1 life per Cat that doesn't want to be adopted by you!")

# this function will randomize the order in which the cats appear in the game
def htrcatlist():
    htrcats = happy_tails_cats()
    random.shuffle(htrcats)
    return htrcats

# I have an intro line for each cat within the dictionary and this function will call it in my main function
def introduce_cat(cat):
    print(cat['intro'])  # add cat intro statement calling from dictionary
    print()
    print("   >^.^<   ")

# this is for the user input values! will be run 5 times within the main code
def get_choice():
    print("Choose which interaction you like to do with me: 1. Brush, 2. Pet, 3. Play, 4. Give a treat")
    useraction = int(input("What would you like to do? Type the number for the action."))
    return useraction

# I separated out the actions to make the code less cluttered (followed Rachel's guide for coding this section)
def do_action(choice, cat, points):
    doesLike = cat['actions'][choice]['likes']
    if doesLike:
        print()
        print("MROW, I love it!")
        print()
        points += 1
    else:
        print()
        print("HISS! I don't want that ")
        points -= 0
    return points

# this is the main function for my location
def main(userstate):
    # these lines will call the userstate values from the game file into my main function
    username = userstate['username']
    points = userstate['points']
    cats_collected = userstate['cats_collected']
    lives = userstate['lives']
    print("***************************************************************************************************************************************")        
    print()
    print('    >^.^<')
    print("Hello " + username)
    # calling the premade function
    welcome_message()
    print("***************************************************************************************************************************************")        
    print()
    import random
    for catdictionary in htrcatlist():
        introduce_cat(catdictionary)
        for x in range(0,5):
            # GARY will come home with the user even with negative interactions.
            # calling the premade functions and defining them to varibles; choice is used in points so it has to be defined first!
            choice = get_choice()
            points = do_action(choice, catdictionary, points)
        #### I tried to fix this if statement section for hours and could not get it to work, and our group looked at it and couldn't figure out what was wrong
        #### 
        if points >= 3:
        # if points == 5: <-- this was the original 'if' statement matching the removed elif statements below
            cats_collected.append(catdictionary['name'])
            print("I'd love to come home with you!!")
        # This section of code I could not get to work, it skips over it no matter what I change
        # elif points == 4:
        #     chance = random.randint(1,10)
        #     if chance <= 2:
        #         print("Hmm, I'm not feeling like leaving Happy Tails today. Sorry!")
        #     else:
        #         cats_collected.append(catdictionary['name'])
        #         print("I'd love to come home with you!!")
        # elif points == 3:
        #     chance = random.randint(1,10)
        #     if chance <= 4:
        #         print("Hmm, I'm not feeling like leaving Happy Tails today. Sorry!")
        #     else:
        #         cats_collected.append(catdictionary['name'])
        #         print("I'd love to come home with you!!")
        # the following statement i tried as elif points <= 2: and else: and nothing worked to make the cat not want to come home with the user..
        elif points <= 2:
            print("I'd rather stay here. Bye!")
            print()
            print("Displeasing the cat has cost you a life!")
            lives -= 1
            print("You now have " + str(lives) + " lives left."  )
        if lives <= 0:
            break
        print()
        print()
        print("***************************************************************************************************************************************")        
        print()
    print("Congratulations, you now have " + str(points) + " points.")
    return {'points': points, 'cats_collected': cats_collected, 'username': username, 'lives': lives}

# DON'T DELETE THIS?
if __name__ == '__main__':
    userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives':9}
    main(userstate['points'], userstate['cats_collected'], userstate['username'], userstate['lives'])
#     #(username, points, cats_collected, lives)



# from master file
#defining print_intro as a funtion
# def print_intro():
#     print('=^..^=     ','=^..^=     ','=^..^=     ' )
#     print('      =^..^=     ','=^..^=     ')
#     print("Welcome to 'PURRfect Pals'")
#     print()
#     print(' =^..^= ')
#     print("Get ready to meet and adopt feline friends from four different cat rescues.")
#     print("Each cat is looking for their furrever home, will you be the purrfect match?")

# from master file
# sets up user variables!
# def main():
#     #random.shuffle returns the list in a random order
#     location = ["Rachel", "Vince", "Kendyll", "Carol"]
#     random.shuffle(location)
#     print(location)

#     #user state to retain and hold accrued points and cats
#     #dictionary to get passed around location files and hold the state of the game
#     userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives':9 }

#     #call in print_intro
#     print_intro()

#     #get the user's name
#     print()
#     userstate['username'] = str(input("  Howdy there! What is your name? "))
#     print()

#if lives is <= 0 then GAME OVER MAN
# def main(end_statements, userstate):
#   lives = int(userstate['lives'])
#   if lives <= 0:
#     print("You've run out of lives!")
#     print("GAME OVER")
#     print("You adopted the following cats:"+ userstate['cats_collected'] + "!")
#     print("Purr points collected:" + userstate['purr_points'])
#   else:
#     print("You adopted the following cats:"+ userstate['cats_collected'] + "!")
#     print("Purr points collected:" + userstate['purr_points'] + ";  Lives remaining:" + userstate['lives'])

# print("""
#          *                  *
#              __                *
#           ,db'    *     *
#          ,d8/       *        *    *
#          888
#          `db\       *     *
#            `o`_                    **
#       *               *   *    _      *
#             *                 / )
#          *    (\__/) *       ( (  *
#        ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
#       | @|  ={      }= | @|  / / | @|o |
#      _j__j__j_)     `-------/ /__j__j__j_
#      ________(               /___________
#       |  | @| \              || o|O | @|
#       |o |  |,'\       ,   ,'"|  |  |  |  hjw
#      vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
#                 _) )    `. \ /
#                (__/       ) )
#                          (_/
# """)
