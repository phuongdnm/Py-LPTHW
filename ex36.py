from sys import exit

### START:
def start_room():
    print "\n"
    print "You're in a dark room. There are two doors in front of you:"
    print "Left and right door. Which would you go?"
    door = raw_input("> ")
    if "left" in door:
        lion_room()
    elif "right" in door:
        Cthulhu_room()
    else:
        "Okay, stay here forever :))"
        exit(0)

def lion_room():
    print "\n"
    print "In this room, you see a sleeping lion." 
    print "That hasn't ate anything for 1000 year."
    print "What are you going to do?"
    print "1. Taunt the lion."
    print "2. Eat your head."
    print "3. Just come to the door after the lion to continue."
    choice = raw_input("> ")

    if choice == "1" or "taunt" in choice:
        dead("The lion wake up and slap your face off.")
    elif choice == "2" or "my" in choice:
        dead("Tasty, isn't it?")
    elif choice == "3" or "come" in choice or "next door" in choice or "continue" in choice:
        print "Haha you defnitely know my joke :))"
        print "The lion that hasn't ate anything for 1000 year is dead."
        print "Open door to continue!"
        raw_input("> ")
        long_door()
    else:
        type_mistake()

def Cthulhu_room():
    print "\n"
    print "In front of you, there is a huge monster Cthulhu."
    print "You scream out loud, then you go insane!"
    print "What do you do now? The evil has noticed you."
    print "1. Run swiftly for your life."
    print "2. Come back to the last room."
    choice = raw_input("> ")

    if choice == "1" or "run" in choice:
        print "\n"
        print "You stray into a high long strair."
        print "You walk through the stair, then you see a long way."
        print "After waling for 2 minutes, you see a bridge."
        bridge_below()
    elif choice == "2" or "come back" in choice or "last room" in choice:
        print "The monster Cthulhu nearly gets your legs off."
        start_room()
    else:
        type_mistake()



### MIDDLE: 
def long_door():
    print "\n"
    print "There is too dark here. But wait!!!"
    print "You see a light from an old man sit next to a bridge."
    print "He told you there was an mysterious treasure in the castle."
    print "He also recommended you to come to the bridge instead of going ahead."
    print "Which is your choice?"
    choice = raw_input("> ")
    if "bridge" in choice or "old man" in choice:
        bridge_top()
    if "ahead" in choice or "continue" in choice:
        gold_room()

def bridge_top():
    print "\n"
    print "You have been lied. The old man is a witch."
    print "After crossing the bridge, you see 2 ways before you: right and left"
    print "Which way do you go?"
    choice = raw_input("> ")
    if "right" in choice:
        Cthulhu_room()
    elif "left" in choice:
        dragon_room()
    else:
        type_mistake()

def bridge_below():
    print "\n"
    print "Now you see 2 way: go ahead or turn left."
    choice = raw_input("> ")
    if "ahead" in choice:
        dragon_room()
    elif "left" in choice:
        pole_top()
    else:
        type_mistake()

def pole_top():
    print "\n"
    print "Ater crossing the bridge, you notice 2 ways: right and left."
    print "Which way do you go?"
    choice = raw_input("> ")
    if "left" in choice:
        lion_room()
    elif "right" in choice:
        gold_room()
    elif "back" in choice:
        bridge_below()
    else:
        type_mistake()



### LAST:
def gold_room():
    print "\n"
    print "You go and see a big room in front of you."
    print "\"This room must be the treasure room \", you said."
    print "But it requires a pass word to open."
    print "Password consist of 4 numbers, try to guess the password:"
    
    password = "1234"
    check = False
    while not check:
        num = raw_input("Your passwords numbers is: > ")
        if num == password:
            print "Congratulation! The door is opening automatically!"
            take_gold()
            check = True
        else:
            print "Wrong. Try again."

def take_gold():
    print "\n"
    print "There is a lot of gold here, how much would you take?"
    how_much = int(raw_input("> "))

    if how_much < 50:
        print "You're not greedy. Good job!"
        print "You won this game."
    elif how_much >= 50:
        print "You greedy bastard!"
    else:
        type_mistake()

def dragon_room():
    print "\n"
    print "In this room, a huge Dragon is guarding a room."
    print "What do you do now?"
    print "1. Feed him a meat."
    print "2. Taunt him."
    print "3. Come back to save your life."

    choice = raw_input("> ")
    if "1" in choice or "feed" in choice:
        print "Where do you get a meat???"
        print "The dragon eat your legs. Game over!"
    elif "2" in choice or "taunt" in choice:
        print "You go insane. The dragon doesn't care about you."
        print "Then he got to sleep. You come to the room after him."
        gold_room()
    elif "3" in choice or "come back" in choice or "save" in choice:
        bridge_below()
    else:
        type_mistake()



### BONUS:
def type_mistake():
    print "I can't understand what you're typing."
    print "Try using thouse directions."


def dead(why):
    print why, "Haha, good job!"
    print "Game over!"
    exit(0)

def map():
    print """
--------------------------------------------------------------------------------
        |                     *old man                                         |
    left|  Lion   |-------------------|    |-----------|                       |
        |         |*******************| B  |***********|       Gold room       |
 Dark   |         |*******************| r  |***********|                       |
 Room   |---------|*******************| i  |***********|-----------------------|
        |         |*******************| d  |***********|                       |
        |Cthulhlhu|*******************| g  |***********|       Dragon room     |
   right|         |*******************| e  |***********|                       |
        |         |-------------------|    |-----------|                       |
        |                                                                      |
--------------------------------------------------------------------------------
"""

map()
start_room()
