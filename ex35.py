from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

#    next = raw_input("> ")
#    if "0" in next or "1" in next:
#        how_much = int(next)
#    else:
#        dead("Man, learn to type a number.")
    """ Here are the bug of this code: python will notice numbers includes "1"
    and "0" character. It means: 1000, 2010, 3315 will work, but 4567, 3349
    won't work beacause they don't have "1" nor "0" in.
    """
# Here's my method:
    how_much = int(raw_input("> "))

    if how_much < 50: 
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
# It's always true, so this part of the game will run again and again.
# This is an infinite loop :))
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
            """ - This line must be here to end the non-stop while-loop because  
            "bear_moved" is now False, then "not bear_moved" means True. "taunt bear" and 
            True are always True, so the loop will print "The bear has moved..." forever. 
                - So this line turn "bear_moved" to True, then "not bear_moved" will be False.
            The loop will stop and JUMP back to the begining. You won't see the line "The
            bear has moved..." again. 
            Is that clear?
            """
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        flee()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def flee():
    while True:
        print "There is too dark. Which would you do: run or comeback?"
        choice = raw_input("> ")

        if "run" in choice:
            start()
        elif "comeback" in choice : 
            print "The evil has left his castle!"
            print "You come into a room which is in front of you."
            gold_room()
        else: 
            print "I don't know what you're doing."
            dead("Ok.")

def dead(why):
    print why, "Good job!"
    exit(0)
"""It's important to close this function because this function "dead" are used
in a INFINITE WHILE-LOOP. Try how you can get out when play the game without
this line. You can't.
    The number in exit() is to define how many error you want to show in screen
Don't worry about it"""


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def helpme():
    print """           
----------------------------------------
|                                      |                        
|                                      |                   
|           GOLD room                   |         Dark space           
|                                       |Door                       
|                                       |                        
|                                      |                        
|-------------______-------------------|----------    ----------|
|              Door                    |                        |
|                                      |      Cthulhu ROOM      |
|                   BEAR room          |                        |
|                                      |                        |
|                                      |                        |
|                   Left Door >        |       < Right Door     |
--------------------------------______---______------------------
|                                                               |
|                                                               |
-----------------------------------------------------------------
                                   Dark Room
          """
helpme()
print "*" *10, 
print "MAP", 
print "*"*10,
print "\n"
start()