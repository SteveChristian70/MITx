# Removing duplicates in Lists

def removeDups(L1, L2):
	for e1 in L1:
		if e1 in L2:
		L1.remove(e1) # Removes by mutating
		
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]	

removeDups(L1, L2)

print (L1) 
# should return [2, 3, 4]	

# Using Clones to save original 

def removeDupsBetter(L1, L2):
	L1Start = L1[:] # makes a copy of the list
	for e1 in L1Start:
		if e1 in L2:
			L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDupsBetter(L1, L2)

print(L1)
# should return [3, 4]
	