print("Welcome to the rollercoaster!")
height=int(input("Enter height"))
if height>120:
  print("Can ride")
  age=int(input("Age? "))
  if age<12:
    print("Pay $5")
    bill=5
  elif age<=18 or age>45 or age<55:
    print("Pay $7")
    bill=7
  else:
     print("Pay $12")
     bill=12
  
  photos=(input("Want Photos? "))
  if photos=="yes":
    print("Pay $3")
    bill+=3
  elif photos=="no":
    print(f"final bill is {bill}")
else:
  print("Can't ride")
