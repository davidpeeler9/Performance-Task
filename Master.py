import list
import math

IsPrime = 0
IsPerfectSquare = 0
DivisorsList = []
PFList = []

while True
  InputNumber = input('What number would you like to test?')
  if isinstance(InputNumber, int) = True:
  	if InputNumber > 1:
			break
return;

def PrimalityTest(y):
  for num in range(1, y/2):
    if InputNumber%num == 0:
      DevisorsList.append(num)
	DevisorsList.append(y)
	if len(DevisorsList) == 2:
		IsPrime == 1
	else:
		IsPrime == 0
return;

def IsPerfectSquare(x):
   if math.sqrt(x)%2 == 0:
      IsPerfectSquare = 1
  else:
      IsPerfectSquare = 0
return;

def PrimeFactorization(): #TODO, change the divisible factors of PFList to primes
	if IsPrime = 0:
		PFList == DevisorsList
	else:
		for item in PFList:
				PrimalityTest(item)
return;

PrimalityTest(InputNumber)
	return;
IsPerfectSquare(InputNumber)
	return;
PrimeFactorization()
	return;

if IsPrime == 0:
	print("% is not a prime number") % InputNumber
else:
	print("% is a prime number") % InputNumber
return;

if IsPerfectSquare == 0:
	print("% is not a perfect square") % InputNumber
else:
	print("% is a perfect square") % InputNumber
return;

print("%'s prime factorization is %") % (InputNumber, PFList)
