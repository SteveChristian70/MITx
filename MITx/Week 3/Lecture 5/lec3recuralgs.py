#recursive algorithm
def recurMul(a, b):
	if b == 1:
		return a
	else:
		return a + recurMul(a, b-1)
		#recursive step above
		
print recurMul(3, 5)
#should return 15