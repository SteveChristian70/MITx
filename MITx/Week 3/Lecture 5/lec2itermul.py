#succesive addition
#a,b could be any number
def iterMul(a, b):
	#current value of computation needs to be set ie. 0
	result = 0 
	while b > 0:
		result += a #updates could be + - % or *
		b -= 1 #takes 1 away from b
	return result