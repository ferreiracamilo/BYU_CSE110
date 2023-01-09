print("\nPlease enter the following:\n")

adjectiveInput = input("adjective: ")
animalInput = input("animal: ")
verbInput1 = input("verb: ")
exclamationInput = input("exclamation: ").capitalize()
verbInput2 = input("verb: ")
verbInput3 = input("verb: ")

print("\nYour story is:\n")

message = "The other day, I was really in trouble. It all started when I saw a very " + adjectiveInput + " " + animalInput + " " + verbInput1 + " down the hallway. " + exclamationInput + "! I yelled. But all I could think to do was to " + verbInput2 + " over and over. Miraculously, that caused it to stop, but not before it tried to " + verbInput3 + " right in front of my family."

print (message)