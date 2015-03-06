balance = 3329
annualInterestRate = 0.2
balanceCopy = balance
monthlyInterestRate = annualInterestRate/12
minPay = 0

monthlyLower = balance/12
monthlyUpper = (balance*(1+monthlyInterestRate)**12)/12
while balance > 0:
	balance = balanceCopy
	minPay += 10
	for i in range(12):
		monthlyUnpaid = balance - minPay
		balance = monthlyUnpaid + monthlyInterestRate*monthlyUnpaid

print "Lowest payment: " + str(round(minPay,2))