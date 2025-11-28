print("====================================")
print("     WELCOME TO CITY CINEMA APP     ")
print("====================================")

# yeh naam puchega
name = input("Apna naam likho: ")

# yeh age puchega
age = int(input("Apni age likho: "))

# yeh tickets ki sankhya puchega
tickets = int(input("Kitne ticket chahiye: "))

print("\nShow Time Chuno:")
print("1. 10:00 AM")
print("2. 1:00 PM")
print("3. 4:00 PM")
print("4. 8:00 PM")

# yeh show time ka option lega
show = input("Show number likho (1-4): ")

# yeh show time set karega
if show == "1":
    show_time = "10:00 AM"
elif show == "2":
    show_time = "1:00 PM"
elif show == "3":
    show_time = "4:00 PM"
else:
    show_time = "8:00 PM"

# yeh age ke hisab se price set karega
if age < 12:
    price = 100    # bachho ka ticket
elif age < 18:
    price = 120    # teenager ka ticket
else:
    price = 150    # adult ka ticket

# total bill banega
total = tickets * price

print("\n====================================")
print("         BOOKING DETAILS            ")
print("====================================")
print("Cinema: City Cinema")
print("Name:", name)
print("Age:", age)
print("Show Time:", show_time)
print("Tickets:", tickets)
print("Price per Ticket:", price)
print("Total Amount:", total)
print("====================================")
print("        ENJOY YOUR MOVIE!           ")
print("====================================")
