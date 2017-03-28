# TODO:
# Clear the console after every test (probably a console issue?)

# Finished:
# Menu
# PrimeFactorization
# PrimalityTest
# SplitNumber
# PerfectSquare
# CircularPrime
# Doesnt check if the menu input is 1-5

import math
import os
import itertools

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  return

def findLowestFactor(y): #Finds lowest factor + corresponding factor
  for item in range(2, int(y)//2):
    if y/item % 1 == 0:
      resultingList = [item, y//item]
      return resultingList

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
	if isPrime(y) is True:
	  print(str(y) + " has no true factors other than 1 and itself.")
	
	for num in range(2, math.ceil(math.sqrt(y))):
	  if y % num == 0:
	    print(str(y) + " equals " + str(num) + " times " + str(y//num))
	return

def IsPerfectSquare():
  y = int(input("What number would you like to test?"))
  if math.sqrt(y)%1 == 0:
    print(str(y) + " is a perfect square, and its root is " + str(math.sqrt(y)))
  else:
    print(str(y) + " is not a perfect square")
  return

def PrimeFactorization(): 
  y = int(input("What number would you like to test?"))

  factorList = [y] #Start out with the inputted interger
  for item in factorList: #Have this repeat till all the items in the array are prime
    if isPrime(item) is False: #If this item is not a prime
      factorList.extend(findLowestFactor(item)) #Insert/Extend the list so that its not a list
      factorList.remove(item) #Remove that item from the list since it has already been broken down
  print(factorList)
  return
  
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
  print("1. Find True Factors")
  print("2. Perfect Square?")
  print("3. Prime Factorization")
  print("4. Circular Prime?")

  choice = input("Choose an option:")
  
  if 1 > int(choice) or 4 < int(choice):
    print("Please choose a valid option.")
    cls()
    Menu()
  if choice == "1":
    FindTrueFactors()
  if choice == "2":
    IsPerfectSquare()
  if choice == "3":
    PrimeFactorization()
  if choice == "4":
    CircularPrime()
  
  choice2 = input("Would you like to run another test?")
  if choice2 == "yes":
    Menu()
  else:
    print("Bye Bye!")

  return


Menu()
