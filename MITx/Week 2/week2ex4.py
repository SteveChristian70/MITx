#1 
num = 10 
for num in range(5):
	print num
print num

#2

divisor = 2 
for num in range(0, 10, 2):
	print num/divisor

#3

for variable in range (20):
	if variable % 4 == 0:
		print variable
	if variable % 16 == 0:
		print 'Foo!'

#4 

for letter in 'hola':
	print letter

#5 

count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count