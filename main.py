from enum import Enum
import sys

change = {
	0.01: 'PENNY',
	0.05: 'NICKEL',
	0.10: 'DIME',
	0.25: 'QUARTER',
	0.50: 'HALF DOLLAR',
	1: 'ONE',
	2: 'TWO',
	5: 'FIVE',
	10: 'TEN',
	20: 'TWENTY',
	50: 'FIFTY',
	100: 'ONE HUNDRED'
}

# Invert 
inv_change = {v: k for k, v in change.items()}

def Compare(PurchasePrice, CashPaid):
	# handle the easy cases
	if (PurchasePrice > CashPaid):
		print("ERROR")
		return

	if (PurchasePrice == CashPaid):
		print("ZERO")
		return

	difference = CashPaid - PurchasePrice
	key = 0
	amount = 0

	while(difference != 0):
		for k, v in reversed(sorted(change.items())):
			
			if(difference % k == 0):
				key = k
				amount = int(difference / k)
				difference = 0
				break
			print(k)

		difference = 0

	print(f"""{amount} {change[key]}""")
	return


for line in sys.stdin:
	#expecting two values, separated by a comma
	values = line.split(",")
	#first value should be purchase price, the other should be the cash paid by the customer
	#both values could have decimals (change), so convert them from string into float data types
	PP = float(values[0])
	CH = float(values[1])
	#call the compare method
	Compare(PP, CH)