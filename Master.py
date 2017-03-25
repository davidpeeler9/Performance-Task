# TODO:
# BaseChanger
# PrimeFactorization
# SplitNumber
# Doesnt check if the menu input is 1-5
# Clear the console after every test
#
# Finished:
# Menu
# PrimalityTest
# PerfectSquare
# Doesnt repeat to menu indefinately

import math
import os



def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  return

def isPrime(x):
  for num in range(2, x//2):
    if x%num == 0:
      return False
    else:
      return True 

def SplitNumber(x):
  x = str(x)
  DigitList = []
  for y in range(len(x)):
    DigitList.insert(1, x[y])
  return DigitList

def FindTrueFactors():
	y = int(input("What number would you like to test?"))
	for num in range(2, math.ceil(math.sqrt(y))):
	  if y % num == 0:
	    print(str(y) + " equals " + str(num) + " times " + str(y//num))
	return

def BaseChanger():
  y = int(input("What number would you like to test?"))
  x = int(input("What base is your starting number?"))
  z = int(input("What base would you like to change into?"))
  return #TODO

def IsPerfectSquare():
  y = int(input("What number would you like to test?"))
  if math.sqrt(y)%1 == 0:
    print(str(y) + " is a perfect square, and its root is " + str(math.sqrt(y)))
  else:
    print(str(y) + " is not a perfect square")
  return

def PrimeFactorization(): 
  y = int(input("What number would you like to test?")) # TODO

def CircularPrime(): #TODO
  y = input("What number would you like to test?")
  
  # Test if the number is prime
  if isPrime(y) is True:
    return print(str(y) + "is not a circular prime.")
  
  DigitList = SplitNumber(y)
  tests = len(SplitNumber(y)) #test every number of digits till tests?
  
  for x in range(tests):
    for num in DigitList:
      
  
  
  
  #Test if the individual digits are prime  
  #for x in SplitNumber(y):
  #  testNumber = int()
  
  #Test if the two number digits are prime
  #  testNumber = int(str(x) + str())
        return #TODO #TODO


# Menu
def Menu():
  print("Welcome to the BONEZONE")
  print("1. Find True Factors")
  print("2. Base Changer")
  print("3. Perfect Square?")
  print("4. Prime Factorization")
  print("5. Circular Prime?")

  choice = input("Choose an option:")

  if choice == "1":
    FindTrueFactors()
  if choice == "2":
    BaseChanger()
  if choice == "3":
    IsPerfectSquare()
  if choice == "4":
    PrimeFactorization()
  if choice == "5":
    CircularPrime()
  
  
  cls()
	
  choice2 = input("Would you like to run another test?")
  if choice2 == "yes" or "y" or "ye":
    Menu()
  else:
    print("Bye Bye!")

  return

Menu()
