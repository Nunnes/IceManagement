#!/usr/bin/env python

class TransactionDTO:
	# Clients' transactions and debts #
	def __init__(self, clientFirstName, clientLastName, quantity, price, credit = 'N'):
		# transaction data transfer objet #
		self.clientFirstName = clientFirstName
		self.clientLastName = clientLastName
		self.quantity = quantity
		self.price = price

		if(credit.lower().strip() == 'y'):
			self.credit = True;
		else: 
			self.credit = False;
		
	
