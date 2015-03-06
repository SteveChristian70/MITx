def applyToEach(L, f):

'''assumes L is a list, f a function
mutates L by replacing each element
e, of L by f(e)'''

for i in range(len(L)):
	L[i] = f(L[i])
	
applyToEach(L, int)
print (L)