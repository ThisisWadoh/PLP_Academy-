def calculator():
    while True:
        print("\nBasic Calculator Program!")

        #Get Input numbers 
        try:
            num1 = float(input("Enter first number:  "))
            num2 = float(input("Enter second number:  "))
        except ValueError:
            print("Invalid input. Numeric values only!")
            continue

        #Choose operation
        print("\nChoose your operation!")
        print("+. Addition")
        print("-. Subtraction")
        print("*. Multiplication")
        print("/. Division")

        operation = input("Enter your choice (+, -, *, /):  ").strip().upper()

        #Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1/num2
            else:
                print("Division by zero not allowed!")
                continue
        
        else: 
            print("Invalid Operation!")
            continue

        #Dispaly Result
        print(f"The result of {num1} {operation} {num2} is: {result}")

        #Another Calculation?
        try_again = input("\nWould you like to perform another calculation? (yes/no): ").strip().upper()
        if try_again == "yes":
            calculator()
        else:
            print("Till next time. Goodbye!")
            break
        
calculator()




