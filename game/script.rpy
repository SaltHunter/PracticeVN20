# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define a = Character("Alice")


# The game starts here.


# TODO_1: Make a simple Visual Novel with Menu Choices of Y and N where one choice leads to one route
# TODO_2: Enhance on the concept, make 5-10 choices, which a combination of say 10 choices would lead to one heroine.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "what's up blyat, what are we doin today?"

    menu choice1:
     "what do you want to do for today?"

     "kill some annoying cunts in the office.":
        e "should be fun ill grab my bazooka."
        jump killchoice
     
     "make new coffee potions.":
        e "errr last time we did that our lab blew up because you added baking soda."
        jump coffee
     
     "Go back home":
        e "dood u just got here."
        jump home
    
    

label killchoice:
    "So i killed everyone in the office and went home afterward."
    jump home

label coffee:
    "So i made a new coffee brew and went home."
    jump home

label home:
    e "and here we are :V, were taking the day off huh."


    "Morning what's on todays schedule"

    menu choice2:
        "What are you going to do?"

        "Get food stocked up":
            e "now that you mention it the fridge is almost empty thanks to you making weird potions in the lab almost everytime"
            jump supermarket

        "hack into CN's Government military server and grab they're confidentials":
            e "sounds fun lets screw them up for ruining our favorite culture and games"
            jump basecamp
        
        "Beat your old min*craft speedrun records":
            e "are you serious right now"
            jump home2


label supermarket:
    "Getting instant noodles and other ingredients"
    jump home2

label basecamp:
    "got a lot of suspicious weapon blueprints and other stuff that we could use to press them"
    jump home2

label home2:
    e "4 runs in 6 hours, and u still havent broken the latest record"



# hello
# blyat
# This ends the game.


return
