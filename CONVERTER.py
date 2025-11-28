while True:
    print("""
    1. hours to minutes
    2. miles to kilometers
    3. kilograms to pounds
    4. degree to radian
    5. celsius to fahrenheit
    6. inch to centimeter
    7. BMI calculator
    8. dollar to rupees
    9. rupees to dollar
    10. feet to meter
    11. exit
    """)

    choice = input("enter your choice: ")

    if choice == "1":
        hours = input("enter hours: ")
        minutes = int(hours) * 60
        print(hours, "hours is", minutes, "minutes")

    elif choice == "2":
        miles = input("enter miles: ")
        kilometers = float(miles) * 1.60934
        print(miles, "miles is", kilometers, "kilometers")

    elif choice == "3":
        kg = input("enter kilograms: ")
        pounds = float(kg) * 2.20462
        print(kg, "kg is", pounds, "pounds")

    elif choice == "4":
        degree = input("enter degree: ")
        radian = float(degree) * 0.0174533
        print(degree, "degree is", radian, "radian")

    elif choice == "5":
        celsius = input("enter celsius: ")
        fahrenheit = (float(celsius) * 9/5) + 32
        print(celsius, "celsius is", fahrenheit, "fahrenheit")

    elif choice == "6":
        inch = input("enter inch: ")
        cm = float(inch) * 2.54
        print(inch, "inch is", cm, "centimeter")

    elif choice == "7":
        weight = float(input("enter weight in kg: "))
        height = float(input("enter height in meters: "))
        bmi = weight / (height * height)
        print("Your BMI is:", bmi)

    elif choice == "8":
        dollar = float(input("enter dollar: "))
        rupees = dollar * 84.50
        print(dollar, "USD is", rupees, "INR")

    elif choice == "9":
        rupees = float(input("enter rupees: "))
        dollar = rupees / 84.50
        print(rupees, "INR is", dollar, "USD")

    elif choice == "10":
        feet = float(input("enter feet: "))
        meter = feet * 0.3048
        print(feet, "feet is", meter, "meters")

    elif choice == "11":
        print("exiting the converter, thank you")
        break

    else:
        print("invalid choice, try again")
        
