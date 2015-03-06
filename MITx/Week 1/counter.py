def months(n):
	count = 0
	while n >= 12:
		count = count + 1
	return count
	
print "This is the number of Months: ", + months()