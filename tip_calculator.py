print("Welcome to the tip calculator!")
a=float(input(print("What was the total bill?\n")))
b=float(input(print("How much tip would you like to give? 10, 12, or  15? \n")))
c=a+b
d=float(input(print("How many people to split the bill? ")))
e=round(c/d,2)
print(f"Each person should pay:$ {e}")