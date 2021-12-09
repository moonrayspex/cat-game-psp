#Geom 67 2021
#  Group 2 Purrfect Pals Computer Terminal Game
#Rachel's code for Gary's Cat Cafe location
#component file for main Purrfect Pals computer game  
#version 3.0
#cat ascii art from: #http://www.ascii-art.de/ascii/c/cat.txt

import random

#list of dictionaries for cats at Gary's cat cafe
#each cat dictionary has their attributes and subdictionary for action attributes
def gary_cats():
    return [
            {
                'name': 'Periwinkle',
                'color': 'blue-point',
                "breed": "Siamese",
                "personality": "cuddly",
                'age': "senior",
                'actions': [
                    { 'actionName': 'brushing', 'likes': True },
                    {'actionName': 'pets', 'likes': True},
                    {'actionName': 'othercats', 'likes': True},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treats', 'likes': False},
                ]
            },
            {
                'name': 'Tabitha',
                'color': 'orange',
                "breed": "short-hair",
                "personality": "athletic",
                'age': "adult",
                'actions': [
                    { 'actionName': 'brushing', 'likes': False },
                    {'actionName': 'pets', 'likes': True},
                    {'actionName': 'othercats', 'likes': False},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treats', 'likes': True},
                ]
            },
            {
                'name': 'SugarPaws',
                'color': 'tuxedo',
                "breed": "short-hair",
                "personality": "shy",
                'age': "kitten",
                'actions': [
                    { 'actionName': 'brushing', 'likes': True },
                    {'actionName': 'pets', 'likes': False},
                    {'actionName': 'othercats', 'likes': True},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treats', 'likes': True},
                ]
            },
            {
                'name': 'Zelda',
                'color': 'seal-point',
                "breed": "Birman",
                "personality": "playful",
                'age': "adult",
                'actions': [
                    { 'actionName': 'brushing', 'likes': True },
                    {'actionName': 'pets', 'likes': True},
                    {'actionName': 'othercats', 'likes': False},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treats', 'likes': True},
                ]
            }
        ]
    

#defining catlist function and assigning a variable to the dictionary.  Random shuffle selecting from the dictionary and returning a selection.
def catlist():
    mycats = gary_cats()
    random.shuffle(mycats)
    return mycats

#introductory message in a function that calls on dictionary keys for the cat selected above. 
def introduce_cat(cat):
    print("Hi, friendly human, I'm " + cat['name'] + " and I'm a " + cat['color'] + ", " + cat['breed'] + " cat, who is very " + cat['personality'] + ". I am a " + cat['age'] + ".  Let's have fun!")  #####add int rest of cat intro statement calling from dictionary keys
    print()
    print("""ฅ^•ﻌ•^ฅ""")

#function for user interaction input. Input is assigned a variable that is returned. 
def get_choice():
    print("Choose how you want to interact with me: 1. Brush, 2. Pet, 3. Play, 4. Give a treat")
    useraction = int(input("What would you like to do? Type the number for the action."))
    return useraction

#function that has 'choice, cat, points'.  a variable is assigned to the retrieval of the selected cat's values for the keys in the set.
#The if-statement relies on boolean logic.  if doesLike is true, then the user gets a point, else the user gets no points. 
def do_action(choice, cat, points):
    doesLike = cat['actions'][choice]['likes']
    if doesLike:
        print()
        print("PURR, I love it!")
        print("""ฅ^•ﻌ•^ฅ""")
        print("Purr-fect!")
        print()
        points += 1
    else:
        print("""
     (\
      ))         )\\
     ((         /  .(
      \\.-"```"'` =_/=
       >  ,       /
       \   )__.\ |
        > / /  ||\\
   jgs  \\ \\  \\ \\
         `" `" `"  `"
                   """)
        print("Boo. HISS. Boo! ")
        print("I just scratched you!")
        points -= 0
    return points

#function for welcome message.  this approach modularizes this component, making easier to modify and move around. 
def print_welcome_message():
    print('=^..^=     ','=^..^=     ','=^..^=     ' )
    print("Welcome to Gary's Cat Cafe.  Each of our cat pals is ready to find their furrever home.  Let's make a match! ")
    print("""
            _,'|             _.-''``-...___..--';)
           /_ \'.      __..-' ,      ,--...--'''
          <\    .`--'''       `     /'
           `-';'               ;   ; ;
     __...--''     ___...--_..'  .;.'
 fL (,__....----'''       (,..--''
     """)

#defining the main program.  the variables call in parts of the dictionary 'userstate' that are carried throughout the gameplay. 
# since those parts of the dictionary are now assigned variables, we can use them for the next steps.
def main(userstate):
    username = userstate['username']
    points = userstate['points']
    cats_collected = userstate['cats_collected']
    lives = userstate['lives']
    print('=^..^=')
    print("Hello " + username)
    print_welcome_message()

    
#defines the catlist function.  the for-loop sets the range of loops that it will complete, 4 loops in this case. 
#the points_collected brings in the variables from above from the previously defined function do_action
#the else-if statement is based on the points accrued.  in this set-up, the user gets immediate feedback on their action and can chose to repeat positive ones to earn more points. 
#the player's dictionary with the key and values is returned at the end, after having gone through the 4-loop game play.  
#after 4-loops with one cat, the game presents another cat
#after 16 actions (having gone through all four cats) the player has exhausted the contents of this file and goes to another location.  
#The userstate dictionary carries over that information to the next location. 
    for catdictionary in catlist():
        points_collected = 0
        introduce_cat(catdictionary)
        print(">>>>>>>>>>>>>>>>>>>>>>> Gamer, you have " + str(points_collected) + " points collected in this round.")
        print('>>>>>>>>>>>>>>>>>>>>>>> Total points ' + str(points))
        for x in range(0,4):
            choice = get_choice()
            points_collected = do_action(choice, catdictionary, points_collected)
            print(">>>>>>>>>>>>>>>>>>>>>>> Gamer, you have " + str(points_collected) + " points collected in this round.")
            print('>>>>>>>>>>>>>>>>>>>>>>> Total Points ' + str(points)) 
        points += points_collected
        if points_collected >= 3:
            cats_collected.append(catdictionary['name'])
            print('=^..^=')
            print("Congratulations! I'm going to be your new roommate.")
            print('=^..^=')
            print('=^..^=')
        elif points_collected < 3:
            print('=^x.x^=     ' )
            print("The cat says, 'No thank you!'. Try another cat")
            print()
            print("Displeasing the cat has cost you a life!")
            print('=^x.x^=     ','=^x.x^=     ','=^x.x^=     ' )
            
            #if statement about to determine if user loses a life and if lives are zero, ending the game.
            lives -= 1
            if lives == 0:
                break
            print("You now have " + str(lives) + " lives left before you die."  )
            print('=^x.x^=     ','=^x.x^=     ','=^x.x^=     ' )
            print()
            print("Congratulations, you have " + str(points) + " points.")
            print()
            print()
            #return the dictionary with the player's stats after gameplay
    return {'points': points, 'cats_collected': cats_collected, 'username': username, 'lives': lives}








#Enables running this file separately from the rest of the game (testing purposes)
#in a closed loop
#DO NOT delete, just comment out
# if __name__ == '__main__':
#     main({'points':0, 'cats_collected':[], 'username':' ', 'lives':9})
#     #(username, points, cats_collected, lives)
