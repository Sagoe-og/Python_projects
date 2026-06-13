# Shopping Cart Program
print("Welcome to the Shopping Cart Program!")

# This program allows users to add items to a shopping cart, view the cart, remove items, and compute the total price.

#declaring the empty lists for price and cart
prices = []
cart = []

#creating a while loop in order to enable the user to continue using the program until he/she decides to exit
while True:
#displaying the menu options

    print()
    
    print ("Please select one of the following : ")
    print ("1. Add item to cart")
    print ("2. View cart ")
    print ("3. Remove item from cart")
    print ("4. Compute Total")
    print ("5. Exit")

    print()

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        item = input("Enter item to add to cart: ")
        item = item.capitalize()  # Capitalize the first letter for consistency
        cart.append(item)
        price = float(input(f"Enter the price of the {item}: "))
        if price < 0:
            print("Price cannot be negative. Please enter a valid price.")
            continue
        prices.append(price)
        print(f"{item} has been added to the cart.")
        
    elif choice == '2':
        if cart:
            print("Items in your cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item} - ${prices[i-1]:.2f}")
        else:
            print("Your cart is empty.")
            
    elif choice == '3':
        if cart:
            item_to_remove = input("Enter item to remove from cart: ")
            item_to_remove = item_to_remove.capitalize()
            # Check if the item exists in the cart
            if item_to_remove in cart:
                index = cart.index(item_to_remove)
                cart.pop(index)
                prices.pop(index)
                print(f"{item_to_remove} has been removed from the cart.")
            else:
                print(f"{item_to_remove} is not in the cart.")
        else:
            print("Your cart is empty.")
            
    elif choice == '4':
        total_price = sum(prices)
        total_items = len(cart)
        print(f"The total price of the items in your cart is: ${total_price:.2f}")
        
    elif choice == '5':
        print("Exiting the shopping cart. Thank you!")
        break
        
    else:
        print("Invalid choice. Please select a valid option (1-5).")
