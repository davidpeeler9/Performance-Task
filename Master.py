import math

IsPrime = 0
IsPerfectSquare = 0
DivisorsList = []
PFList = []

while True:
  InputNumber = input("What number would you like to test?")
  if isinstance(InputNumber, int) == True:
	  break

def PrimalityTest(y):
  for num in range(1, y):
    if InputNumber%num == 0:
      DevisorsList.append(num)
  return

def IsPerfectSquare(x):
  if math.sqrt(x)%2 == 0:
    IsPerfectSquare = 1
  else:
      IsPerfectSquare = 0
  return

def PrimeFactorization(): #TODO, change the divisible factors of PFList to primes
	if IsPrime == 0:
		PFList == DevisorsList
	else:
		for item in PFList:
				PrimalityTest(item)
	return

PrimalityTest(InputNumber)

IsPerfectSquare(InputNumber)
PrimeFactorization()


if IsPrime == 0:
	print("% is not a prime number") % InputNumber
else:
	print("% is a prime number") % InputNumber


if IsPerfectSquare == 0:
	print("% is not a perfect square") % InputNumber
else:
	print("% is a perfect square") % InputNumber


print("%'s prime factorization is %") % (InputNumber, PFList)
