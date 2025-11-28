import math

while True:
    try:
        print("""
╔══════════════════════════════════╗
║            CALCULATOR           ║
╠══════════════════════════════════╣
║ 1. Addition                      ║
║ 2. Subtraction                   ║
║ 3. Multiplication                ║
║ 4. Division                      ║
║ 5. Modulus                       ║
║ 6. Square Root                   ║
║ 7. Power (x^n)                   ║
║ 8. Square (x²)                   ║
║ 9. Cube (x³)                     ║
║ 10. Percentage                   ║
║ 11. Floor Division (//)          ║
║ 12. Absolute Value               ║
║ 13. Factorial                    ║
║ 14. Cube Root                    ║
║ 15. Exit                         ║
╚══════════════════════════════════╝
        """)

        choice = input("Enter your choice (1-15): ")

        # Basic Two-Number Operations
        if choice in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        # Individual Number Operations
        elif choice in ["6", "8", "9", "10", "11", "12", "13", "14"]:
            num1 = float(input("Enter number: "))

        # Power x^n
        elif choice == "7":
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter power: "))

        # ADDITION
        if choice == "1":
            print("Result (Addition):", num1 + num2)

        # SUBTRACTION
        elif choice == "2":
            print("Result (Subtraction):", num1 - num2)

        # MULTIPLICATION
        elif choice == "3":
            print("Result (Multiplication):", num1 * num2)

        # DIVISION
        elif choice == "4":
            if num2 != 0:
                print("Result (Division):", num1 / num2)
            else:
                print("Error: Cannot divide by zero.")

        # MODULUS
        elif choice == "5":
            print("Result (Modulus):", num1 % num2)

        # SQUARE ROOT
        elif choice == "6":
            if num1 >= 0:
                print("Result (Square Root):", math.sqrt(num1))
            else:
                print("Error: Negative number not allowed.")

        # POWER x^n
        elif choice == "7":
            print("Result (Power):", num1 ** num2)

        # SQUARE
        elif choice == "8":
            print("Result (Square):", num1 * num1)

        # CUBE
        elif choice == "9":
            print("Result (Cube):", num1 * num1 * num1)

        # PERCENTAGE (x%)
        elif choice == "10":
            print("Result (Percentage):", (num1 / 100))

        # FLOOR DIVISION
        elif choice == "11":
            print("Result (Floor Division):", num1 // 1)

        # ABSOLUTE VALUE
        elif choice == "12":
            print("Result (Absolute Value):", abs(num1))

        # FACTORIAL
        elif choice == "13":
            if num1 < 0 or num1 % 1 != 0:
                print("Error: Factorial needs a positive whole number.")
            else:
                print("Result (Factorial):", math.factorial(int(num1)))

        # CUBE ROOT
        elif choice == "14":
            print("Result (Cube Root):", num1 ** (1/3))

        # EXIT
        elif choice == "15":
            print("Exiting calculator. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 15.")

    except:
        print("Invalid input! Please enter valid numbers.")
