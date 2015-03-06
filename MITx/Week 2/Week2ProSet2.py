#Month: 1 
#Minimum Monthly Payment: 96.0
#Remaining balance: 4784.0

#start the code

monthlyInterestRate = annualInterestRate/12
totalPaid = 0

for i in range(12):
    minPay = monthlyPaymentRate*balance
    monthlyUnpaid = balance - minPay
    balance = monthlyUnpaid + monthlyInterestRate*monthlyUnpaid
    totalPaid += minPay
    print "Month: "+str(i+1)
    print "Minimum monthly payment: "+str(round(minPay,2))
    print "Remaining balance: " + str(round(balance,2))
    

print "Total paid: "+str(round(totalPaid,2))
print "Remaining balance: "+str(round(balance,2))