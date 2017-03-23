# TODO:
# BaseChanger
# PrimeFactorization
# Doesnt repeat to menu indefinately
#
# Finished:
# Menu
# PrimalityTest
# PerfectSquare
import math

# 1. Finds factors that does not include 1 or y
def FindTrueFactors():
	y = int(input("What number would you like to test?"))
	for num in range(2, math.ceil(math.sqrt(y))):
	  if y % num == 0:
	    print(str(y) + " equals " + str(num) + " times " + str(y//num))
	return

# 2. Changes the base of y
# TODO basically everything
def BaseChanger():
  y = int(input("What number would you like to test?"))
  x = int(input("What base is your starting number?"))
  z = int(input("What base would you like to change into?"))
  return

# 3. Finds the perfect square of y, if it is a whole number, then outputs that it is a perfect square
def IsPerfectSquare():
  y = int(input("What number would you like to test?"))
  if math.sqrt(y)%1 == 0:
    print(str(y) + " is a perfect square, and its root is " + str(int(math.sqrt(y))))
  else:
    print(str(y) + " is not a perfect square")
  return

# 4. Finds the Prime Factors of y
# TODO basically everything
def PrimeFactorization(): #TODO, change the divisible factors of PFList to primes
  y = int()
  return

# Menu
def Menu():
  print("Welcome to the BONEZONE")
  print("1. Find True Factors")
  print("2. Base Changer")
  print("3. Perfect Square?")
  print("4. Prime Factorization")

  choice = input("Choose an option:")

  if choice == "1":
    FindTrueFactors()
  if choice == "2":
    BaseChanger()
  if choice == "3":
    IsPerfectSquare()
  if choice == "4":
    PrimeFactorization()
  return

#Need it to repeat back to menu if user prompts

Menu()

choice2 = input("Would you like to run another test?")
if choice2 == "yes":
  Menu()
else:
  print("Bye Bye!")
  
