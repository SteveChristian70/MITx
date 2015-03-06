#Fibonacci numbers
def fib(x):
	"""assumes x an int >= 0
	returns Fibonacci x"""
	assert type(x) == int and x >= 0  #assert checks to make sure line = true
	if x == 0 or x ==1:
		return 1
	else:
		return fib(x-1) + fib(x-2)