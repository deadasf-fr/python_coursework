print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height > 120:
    print("You can ride")
    age = int(input("Age? "))
    if age <= 18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("Can't ride")
