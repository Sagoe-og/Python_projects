import math
amount = 6568.6889
tax = 0.07

amount2 = round(amount, 2)
cost = amount * tax
print (amount2)
print (f"{amount:.2f}")
print ( f"Total cost: ${cost:.2f}")

big_number = 12345678901234567890
print (f"{big_number: ,} is a very huge number")

deg = math.pi * amount
print (f"{deg:.3f}")
