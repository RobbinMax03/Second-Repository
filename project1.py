#I'm going to write a program that determines whether or not people are available for certain discounts at stores.

#welcoming the shopper and telling them how the program works
def WelcomeShopper():
  print("Welcome to our shop! \nI'm going to ask some questions to see if you are eligible for some discounts!\n")
WelcomeShopper()

#asking user for an answer as to their age and if they are a student
studentYN = str(input("Are you a student right now? "))
age = int(input("Whats your age? "))

#defining the function that will calculate the dicounts
def discount(x,y):
  if ((x == "yes") and (y >= 60)) or ((x == "Yes") and (y >= 60)):
    print("Nice! You are eligible for the student discount as well as the senior discount")
  elif ((x == "no") and (y >= 60)) or ((x == "No") and (y >= 60)):
    print("Sorry, no student discount. But you are eligible for the senior citizen discount.")
  elif ((x == "yes") and (y < 60)) or ((x == "Yes") and (y < 60)):
    print("You are eligible for the student discount")
  elif ((x == "no") and (y < 60)) or ((x == "No") and (y < 60)):
    print("Sorry, no discounts are available for you.")
  else:
    print("Sorry, that's not a valid input")

#calling the function
discount(studentYN,age)
