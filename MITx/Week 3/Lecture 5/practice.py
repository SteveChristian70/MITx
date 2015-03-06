def iterPower(base, exp):
	result = 1 
	while exp > 0:
		result *= base
		exp -= 1
	return result
	
def recurPower(base, exp):
	if exp <= 0:
		return 1
	return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):

	if exp <= 0:
		return 1
	elif exp % 2 == 0:
		return recurPowerNew(base * base, exp/2)
	
	return base * recurPowerNew(base, exp - 1)
	
def gcdIter(a, b):

	testValue = min(a, b)
	
	while a % testValue != 0 or b % testValue != 0:
		testValue -= 1
		
	return testValue
	
def gcdRecur(a, b):
	
	if b == 0:
		return a
	return gcdRecur(b, a % b)