# TODO:
# BaseChanger
# PrimeFactorization
# PerfectSquare
#
# Finished:
# Menu
# PrimalityTest
#
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
  return

# 3. Finds the perfect square of y, if it is a whole number, then outputs that it is a perfect square
# TODO basically everything
def IsPerfectSquare():
  y = int(input("What number would you like to test?"))
  if math.sqrt()%1 == 0:
    print(y + "is a perfect square")
  else:
      PerfectSquare = 0
  return

# 4. Finds the Prime Factors of y
# TODO basically everything
def PrimeFactorization(): #TODO, change the divisible factors of PFList to primes
	if Prime == 0:
		PFList == DivisorsList
	else:
		for item in PFList:
				PrimalityTest()
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

Menu()

choice2 = input("Would you like to run another test?")
if choice2 == "yes":
  Menu()
else:
  print("Bye Bye!")
  
