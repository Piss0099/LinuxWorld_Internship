from colorama import Fore, Style, init
init()

balance = 500000
pin = 2026
password = "Duniyakhatam"
attempts = 0
max_attempts = 3

# UI Colors
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.CYAN
reset = Style.RESET_ALL

print(blue + "\n╔══════════════════════════════╗")
print("║      PYTHON ATM SWAGAT       ║")
print("╚══════════════════════════════╝\n" + reset)

while True:
    while attempts < max_attempts:
        print(yellow + "Login Karein" + reset)

        try:
            user_pin = int(input("PIN Dalein: "))
        except:
            print(red + "PIN number me hona chahiye!" + reset)
            continue

        user_password = input("Password Dalein: ")

        if user_pin == pin and user_password == password:
            print(green + "\nLogin Safal! \n" + reset)
            break
        else:
            attempts += 1
            print(red + f"Galat PIN ya Password! Bachi koshish: {max_attempts - attempts}\n" + reset)

    if attempts == max_attempts:
        print(red + "\nX 3 Baar Galat. ATM Block Ho Gaya!\n" + reset)
        break

    while True:
        print(blue + """
╔════════ ATM MENU ════════╗
║ 1. Balance Dekhein        ║
║ 2. Paise Nikalein         ║
║ 3. Paise Jama Karein      ║
║ 4. Exit                   ║
╚═══════════════════════════╝
""" + reset)

        choice = input(yellow + "Option Dalein (1-4): " + reset)

        if choice == "1":
            print(green + f"\nAapka Balance: ₹{balance}\n" + reset)

        elif choice == "2":
            try:
                amount = int(input("Kitne Paise Nikalne Hain: ₹"))
            except:
                print(red + "Galat Amount! Number Dalein.\n" + reset)
                continue

            if amount <= balance:
                balance -= amount
                print(green + f"Paise Nikal Gaye! Naya Balance: ₹{balance}\n" + reset)
            else:
                print(red + "Balance Kam Hai!\n" + reset)

        elif choice == "3":
            try:
                amount2 = int(input("Kitne Paise Jama Karne Hain: ₹"))
            except:
                print(red + "Galat Amount! Number Dalein.\n" + reset)
                continue

            balance += amount2
            print(green + f"Paise Jama Ho Gaye! Naya Balance: ₹{balance}\n" + reset)

        elif choice == "4":
            print(blue + "\nDhanyavaad! ATM Band Ho Raha Hai \n" + reset)
            exit()

        else:
            print(red + "Galat Option! 1-4 Dalein.\n" + reset)
