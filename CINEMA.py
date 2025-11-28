print("======================================")
print("      WELCOME TO CITY CINEMA APP      ")
print("======================================")

# User Details
name = input("Apna naam likho: ")
age = int(input("Apni age likho: "))
tickets = int(input("Kitne ticket chahiye: "))

# Show Time Selection
print("\nShow Time Chuno:")
print("1. 10:00 AM")
print("2. 1:00 PM")
print("3. 4:00 PM")
print("4. 8:00 PM")

show = input("Show number likho (1-4): ")

if show == "1":
    show_time = "10:00 AM"
elif show == "2":
    show_time = "1:00 PM"
elif show == "3":
    show_time = "4:00 PM"
else:
    show_time = "8:00 PM"

# Pricing Based on Age
if age < 12:
    price = 100
elif age < 18:
    price = 120
else:
    price = 150

# Seat Selection Logic
seats = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5"
]

print("\nAvailable Seats:")
for s in seats:
    print(s, end="  ")

print("\n")
chosen_seats = []

for i in range(tickets):
    while True:
        seat = input(f"Seat {i+1} select karo: ")
        if seat in seats:
            chosen_seats.append(seat)
            seats.remove(seat)
            break
        else:
            print("Seat unavailable ya galat input. Dusra seat try karo.")

# Total Amount
total = tickets * price

# Booking Summary
print("\n======================================")
print("            BOOKING DETAILS           ")
print("======================================")
print("Cinema: City Cinema")
print("Name:", name)
print("Age:", age)
print("Show Time:", show_time)
print("Tickets:", tickets)
print("Price per Ticket:", price)
print("Seats:", ", ".join(chosen_seats))
print("--------------------------------------")
print("Total Amount:", total)
print("======================================")
print("        ENJOY YOUR MOVIE! 🍿🎬        ")
print("======================================")
