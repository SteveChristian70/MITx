'''Define a function isVowel2(char) that returns True if char is a vowel 
('a', 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that 
char is a single letter of any case (ie, 'A' and 'a' are both valid).

This function is similar to the previous problem - but this time, 
do use the keyword in. Your function should take in a single string 
and return a boolean.'''

def isVowel2(char):

	if char in 'aeiouAEIOU':
        return True
        
    else:
        return False