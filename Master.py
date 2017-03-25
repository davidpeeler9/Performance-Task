# TODO:
# BaseChanger
# PrimeFactorization
# Doesnt check if the menu input is 1-5
# Clear the console after every test
# Doesnt repeat to menu indefinately

# Finished:
# Menu
# PrimalityTest
# SplitNumber
# PerfectSquare
# CircularPrime

import math
import os
import itertools

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  return

def isPrime(x):
  FactorList = []
  x = int(x)
  for num in range(2, math.ceil(x//2)):
    if x%num == 0:
      FactorList.insert(1, num)
  if len(FactorList) == 0:
    return True
  else:
    return False

def SplitNumber(x):
  x = str(x)
  DigitList = []
  for y in range(len(x)):
    DigitList.insert(1, (x[y]))
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
  return #TODO #TODO

def IsPerfectSquare():
  y = int(input("What number would you like to test?"))
  if math.sqrt(y)%1 == 0:
    print(str(y) + " is a perfect square, and its root is " + str(math.sqrt(y)))
  else:
    print(str(y) + " is not a perfect square")
  return

def PrimeFactorization(): 
  y = int(input("What number would you like to test?"))
  
  # Testing if it is prime --> true factors would be its PrimeFactorization
  if isPrime(y) is True:
    print("The prime factorization for this number is 1 and " + str(y))
  
def CircularPrime():
  y = int(input("What number would you like to test?"))
  comb = list(map("".join, itertools.permutations(str(y))))
  for item in comb:
    if isPrime(item) is False:
      print(str(y) + " is not a circular prime.")
      break
  else:
    print(str(y) + " is a circular prime.")
  return



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
  
  choice2 = input("Would you like to run another test?")
  if choice2 == "yes":
    Menu()
  else:
    print("Bye Bye!")

  return


Menu()
