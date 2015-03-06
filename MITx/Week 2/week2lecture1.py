#guess and check
x = int(raw_input('Enter and integer:'))

for ans in range(0, abs(x)+1): #generate
	if ans**3 == abs(x):
		break #check 		
if ans**3 != x:
	print(str(x) + ' is not a perfect cube')
else:
	if x < 0:
		ans = -ans
	print ('Cube root of ' + str(x) + 'is ' + str(ans))
