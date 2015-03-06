x = 3
ans = 0
# Binding these together
itersLeft = x
# while loop for boolean
while (itersLeft != 0):
	ans = ans + x
	itersLeft = itersLeft - 1
print (str(x) + '*' + str(x) + '=' + str(ans))