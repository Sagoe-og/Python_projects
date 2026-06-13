# collecting data from the user
print("Please enter the following:")

adjective = input("An adjective: ")
animal = input("An animal: ")
verb = input("A verb: ")
exclamation = input("An exclamation: ")
verb2 = input("Another verb: ")
verb3 = input("Another verb: ")

#writing the story using the collected data 
print("Your story is:")
#added a space between the print statements to make it more readable.
print()
print()

#added string methods to make the story more interesting and readable.
print(f"The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway.")
print(f"{exclamation.capitalize()} I yelled. But all I could think to do was to {verb2.lower()} over and over.")
print(f"Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family.") 