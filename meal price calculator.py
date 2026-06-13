#collecting data from the user
childs_meal = float(input("What is the price of the child's meal? "))
adult_meal = float(input("What is the price of the adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))


#calculating the total cost
print()
print()
Subtotal = (childs_meal * number_of_children) + (adult_meal * number_of_adults)
print (f"Subtotal : ${Subtotal:.2f}")


#calculating the sales tax
print()
print()
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = Subtotal * (sales_tax_rate / 100)
print (f"Sales Tax : ${sales_tax:.2f}")
#calculating the total cost 
Total = Subtotal + sales_tax
print (f"Total : ${Total:.2f}")


#calculating the change
print()
print()
amount = float(input("What is the payment amount ? "))
change = amount - Total
print (f"Change : ${change:.2f}")