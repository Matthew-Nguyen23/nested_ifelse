#In this project it is to learn the if, elif, and else statements with nested if statements!

print("Welcome to the Rollercoaster!")
height = int(input("What is your height?"))

if height >= 120:
  print("You Can Ride the Rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
  
  
else:
  print("You CANNOT ride the Rollercoaster!")