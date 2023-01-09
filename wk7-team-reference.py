import random

random_number = 1 #Start with a prefixed value to go into the loop
number_input = 0 #Start with a prefixed value to go into the loop
number_plays = 0
keep_playing = "none"

while number_input != random_number or keep_playing.lower() == "yes":
    number_plays += 1
    random_number = random.randint(1, 100)
    print(f"What is the magic number? {random_number}")
    number_input = int(input("What is your guess? "))
    if random_number > number_input:
        print("Higher")
    elif random_number < number_input:
        print("Lower")
    else:
        print("You guessed it!")
        print(f"It took you {number_plays} attempt/s")
        keep_playing = "none"
        while(keep_playing != "yes" and keep_playing != "no"):
            keep_playing = input("Do you wanna keep playing (yes/no)? ")
            if keep_playing.lower() == "yes":
                number_plays = 0
            elif keep_playing.lower() == "no":
                break