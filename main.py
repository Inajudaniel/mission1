# DIGITAL TRANSLATOR PROJECT
# Tier 1 - Tier 5


# MAIN MENU

def main_menu():

    while True:
        print("\n================================")
        print("       DIGITAL TRANSLATOR")
        print("================================")
        print("1. Literal Assistant (Breakfast)")
        print("2. ATM Withdrawal")
        print("3. Simple Calculator")
        print("4. Data Translator")
        print("5. Online Store")
        print("6. Exit")
        print("================================")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            breakfast()

        elif choice == "2":
            atm()

        elif choice == "3":
            calculator()

        elif choice == "4":
            data_translator()

        elif choice == "5":
            online_store()

        elif choice == "6":
            print("Thank you for using Digital Translator.")
            break

        else:
            print("Invalid option. Please try again.")


# TIER 1: THE LITERAL ASSISTANT

def breakfast():

    print("\n--- PREPARING BREAKFAST ---")

    print("1. Go to the kitchen.")
    print("2. Get one cup of tea.")
    print("3. Get four slices of bread.")
    print("4. Get a kettle and fill it with water.")
    print("5. Switch on the kettle.")
    print("6. Wait until the water boils.")
    print("7. Put a tea bag into a cup.")
    print("8. Pour the hot water into the cup.")
    print("9. Add sugar and milk if required.")
    print("10. Stir the tea with a spoon.")
    print("11. Put the four slices of bread into the toaster.")
    print("12. Switch on the toaster.")
    print("13. Wait until the bread is toasted.")
    print("14. Remove the toasted bread carefully.")
    print("15. Place the tea and toasted bread on a tray.")
    print("16. Serve the breakfast.")

    print("\nBreakfast preparation completed.")


# TIER 2: ATM WITHDRAWAL

def atm():

    print("\n--- ATM WITHDRAWAL ---")

    balance = 50000
    pin = "1234"

    card = input("Insert your card? (yes/no): ").lower()

    if card != "yes":
        print("Please insert your card to continue.")
        return

    print("Card accepted.")

    entered_pin = input("Enter your PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN. Transaction cancelled.")
        return

    print("PIN verified successfully.")
    while True:
        amount = input("Enter the amount you want to withdraw: ")

        if not amount.isdigit():
            print("Invalid amount.")
            return

        amount = int(amount)
    
        if amount <= 0:
            print("Enter an amount greater than zero.")

        elif amount > balance:
            print("Insufficient account balance.")

        elif amount > 20000:
                print("Amount exceeds the ATM withdrawal limit.\nEnter amount less than 20k.")
                continue
            
    
        else:
            balance = balance - amount

            print("\nTransaction successful!")
            print("Please collect your cash:", amount)
            #print("Your remaining balance is:", balance)
            next = input("do you want to perform another transaction? Yes/no: ").lower()
            if next == Yes:
                continue
            if next == no:
                print("Pleas collect your card")


        print("Please collect your card.")
        break
        


# TIER 3: SIMPLE CALCULATOR

def calculator():

    print("\n--- SIMPLE CALCULATOR ---")

    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice (1-4): ")

    if operation == "1":

        result = number_1 + number_2
        print("Result:", result)

    elif operation == "2":

        result = number_1 - number_2
        print("Result:", result)

    elif operation == "3":

        result = number_1 * number_2
        print("Result:", result)

    elif operation == "4":

        if number_2 == 0:
            print("Error: Division by zero is not allowed.")

        else:
            result = number_1 / number_2
            print("Result:", result)

    else:
        print("Invalid operation.")


# TIER 4: DATA TRANSLATOR

def data_translator():

    print("\n--- DATA TRANSLATOR ---")

    customer_name = "Victor"
    age = 30
    account_balance = 150000.50
    account_active = True

    print("Customer Information")

    print("Name:", customer_name)
    print("Age:", age)
    print("Account Balance:", account_balance)
    print("Account Active:", account_active)

    print("\nData Types")

    print("Name data type:", type(customer_name))
    print("Age data type:", type(age))
    print("Balance data type:", type(account_balance))
    print("Account status data type:", type(account_active))

    print("\nDigital Representation")

    print("Customer name is stored as text.")
    print("Age is stored as an integer.")
    print("Account balance is stored as a decimal number.")
    print("Account status is stored as a Boolean value.")

    print("\nAccount Status Check")

    if account_active:
        print("Victor's account is active.")

    else:
        print("Victor's account is inactive.")


# TIER 5: ONLINE STORE

def online_store():

    print("\n--- ONLINE STORE ---")

    product_name = "Laptop"
    product_price = 50000
    available_quantity = 10

    print("Welcome to our online store.")

    print("\nAvailable Product")
    print("Product:", product_name)
    print("Price:", product_price)
    print("Available Quantity:", available_quantity)

    customer_name = input("\nEnter your name: ")

    quantity = input("How many laptops do you want to buy? ")

    if not quantity.isdigit():
        print("Invalid quantity.")
        return

    quantity = int(quantity)

    if quantity <= 0:
        print("Please enter a quantity greater than zero.")

    elif quantity > available_quantity:
        print("Sorry, we do not have enough products.")

    else:

        total_price = product_price * quantity

        print("\n--- ORDER SUMMARY ---")

        print("Customer:", customer_name)
        print("Product:", product_name)
        print("Quantity:", quantity)
        print("Unit Price:", product_price)
        print("Total Amount:", total_price)

        payment = input("\nHave you made payment? (yes/no): ").lower()

        if payment == "yes":

            available_quantity = available_quantity - quantity

            print("\nOrder confirmed!")
            print("Thank you for shopping with us.")

            print("Remaining Stock:", available_quantity)

        else:

            print("Your order is awaiting payment.")

    print("\nThank you for visiting our online store.")


# RUN THE PROGRAM

main_menu()