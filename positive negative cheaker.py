print("====================================")
print("      NUMBER CHECKING PROGRAM       ")
print("====================================")

while True:
    # number input lega
    num = float(input("Koi number likho: "))

    # check karega number positive, negative ya zero
    if num > 0:
        print(num, "positive number hai")
    elif num < 0:
        print(num, "negative number hai")
    else:
        print("yeh zero hai")

    # replay option
    choice = input("Kya aap fir se number check karna chahte ho? (yes/no): ").lower()
    if choice != "yes":
        print("\n====================================")
        print("         PROGRAM FINISHED           ")
        print("====================================")
        break
