# bisectional number guesser

print "Please think of a number between 0 and 100!"

high = 100
low = 0
guessed = False

while not guessed:

	ans = (high + low)/2
	print "Is your secret number " + str(ans) + "?",
	letter = raw_input("\nEnter 'h' to indicate the guess is too high.\
 Enter 'l' to indicate the guess is too low.\
 Enter 'c' to indicate I guessed correctly.")

	if letter == 'c':
		guessed = True

 	elif letter == 'l':
 		low = ans
 	
 	elif letter == 'h':
 		high = ans
 			
	else:
		print "Sorry, I did not understand your input"
	
	
print "Game over. Your secret number was: " + str(ans)