#Palindrome checker using Recursive method

def isPalindrome(s):

	def toChars(s):  #putting two functions in a function
	s = s.lower()  #s.lower makes sure we use lower case
	ans = '' # ans has to be defined
	for c in s:
		if c in 'abcdefghijklmnopqrstuvwxyz':
			ans = ans + c
		return ans
		
	def isPal(s):
		if len(s) <= 1:
			return True
		else:
		return s[0] == s[-1] and isPal(s[1:-1])  #[0] = 1st letter [-1] last
		
	return isPal(toChars(s))
	
"""call with isPalindrome in idle or 

print isPalindrome(abba)"""