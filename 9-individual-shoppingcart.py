print("Welcome to the Shopping Cart Program!")

input_option = 0
products = []
prices = []
while(input_option != 5):
    temp_price = 1.1
    temp_product = ""
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    input_option = int(input("Please enter an action: "))
    if input_option == 1: #OPTION1 - ADD ITEM
        temp_product = input("What item would you like to add? ")
        temp_price = float(input(f"What is the price of '{temp_product}'? "))
        products.append(temp_product)
        prices.append(temp_price)
        print(f"'{temp_product.capitalize()}' has been added to the cart.") #It was added a capitalize so it looks better cause sentence begins with it
    elif input_option == 2: #OPTION2 - VIEW CART
        if(len(products)==0 and len(prices)==0):
            print("You have not added other products yet") #Added a control to avoid doing unnecessary actions
        else:
            print("The contents of the shopping cart are:")
            for index_for in range(len(products)):
                print(f"{index_for+1}. {products[index_for].capitalize()} - ${prices[index_for]:.2f}") #It was added a capitalize so it looks better cause sentence begins with it
    elif input_option == 3: #OPTION3 - DELETE ITEM
        if(len(products)==0 and len(prices)==0):
            print("You have not added other products yet") #Added a control to avoid doing unnecessary actions
        else:
            option_to_remove = int(input("Which item would you like to remove? "))
            if option_to_remove <= len(products):
                message_template = f"Item '{products[option_to_remove-1]}' was removed -respective price as well has been removed-"
                prices.remove(prices[option_to_remove-1])
                products.remove(products[option_to_remove-1])
                print(message_template)
            else:
                print("Sorry, that is not a valid item number.")
    elif input_option == 4: #OPTION4 - COMPUTE TOTAL
        #The total price of the items in the shopping cart is $7.49
        total_to_print = 0
        for onePrice in prices:
            total_to_print = total_to_print + onePrice
        print(f"The total price of the items in the shopping cart is ${total_to_print:.2f}")
    print()