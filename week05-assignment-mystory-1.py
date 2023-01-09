import random

def roll_dice():
    x = "Y"
    while x == "Y":
        no = random.randint(1, 6)
        print("YOUR DICE THROW IS")
        if no == 1:
            print("[-----------------]")
            print("[                 ]")
            print("[        0        ]")
            print("[                 ]")
            print("[-----------------]")
        elif no == 2:
            print("[-----------------]")
            print("[        0        ]")
            print("[                 ]")
            print("[        0        ]")
            print("[-----------------]")
        elif no == 3:
            print("[-----------------]")
            print("[ 0               ]")
            print("[        0        ]")
            print("[               0 ]")
            print("[-----------------]")
        elif no == 4:
            print("[-----------------]")
            print("[ 0             0 ]")
            print("[                 ]")
            print("[ 0             0 ]")
            print("[-----------------]")
        elif no == 5:
            print("[-----------------]")
            print("[ 0             0 ]")
            print("[        0        ]")
            print("[ 0             0 ]")
            print("[-----------------]")
        elif no == 6:
            print("[-----------------]")
            print("[ 0      0      0 ]")
            print("[                 ]")
            print("[ 0      0      0 ]")
            print("[-----------------]")
        x = input("Press 'Y' to try your luck again and 'N' to exit:")
        print("\n")
    return no


months_sleeping = 5
months_sleeping = int(input("Welcome!! You'll be in an exciting journey on a zombie apocalypse. Provide a whole number: "))

print(f"\n***STORY BEGINGS***\nYou've been sleeping for {months_sleeping} month/s and suddenly woke up.\nFinding out an abandoned city at the darkest hour of night with a broken leg.")

print("\n***1ST TIME TO CHOOOSE***\nChoose your pack from options below -by typing first word-")
print("-GPS (pack includes a flashlight)")
print("-BIKE (pack includes a can of gas)")
pack_chosen = input("My option is: ")
zombie_action1 = ""
zombie_action2 = ""
my_throw_dice = 1000 #Load a number out of range

if pack_chosen.upper() == "GPS":
    print("\n**GAME OVER**")
    print("You ended up without batteries in sewers. There's few steps around ....")
    print("GAME OVER!! You get cauth by a zombie. Better luck for next time.")
    exit()
elif pack_chosen.upper() != "BIKE":
    #WRONG OPTION FLOW
    print("\n**GAME OVER**")
    print("Aggg Arggg Daaa...!!! Brains Brains!!! False alarm folks there was no brain")
    print("GAME OVER!! ANYWAYS ZOMBIES DID NOT EVEN WANNA CHEW YOUR BRAIN?? Choose wisely next time my dear padawan")
    exit()
else:
    print("\n\n***STORY SECOND ACT, CHOOSE WISELY TO SURVIVE!!***")
    print("You drove for a while and decided to")
    print("-MALL > Go to a mall to live there")
    print("-SURVIVORS > Seek for other survivors in a nearby neighborhood")
    
    zombie_action1 = input("My option is: ")


if zombie_action1.upper() == "SURVIVORS":
    print("CONGRATULATIONS!! You started a new town with other survivors")
    exit() #The games finished
elif zombie_action1.upper() == "MALL":
    print("So far you've been able to survive. However is your luck enough...?? Let's roll the dice to know it\n\n")
    my_throw_dice = roll_dice()
    print("You rolled out a " + str(my_throw_dice))
else:
    print("\nReally...? You came so far to surrender so easily.")
    exit()

print("\n\n***STORY THIRD AND FINAL ACT!!***")
if my_throw_dice <= 4:
    print("You go into parking lot to find the mall entrance")
    print("There's few steps around ....")
    print("GAME OVER!! You get cauth by a zombie. Better luck for next time.")
else:
    print("You go into backdoor to find the mall entrance")
    print("CONGRATULATIONS!! You started a new town with other survivors")
