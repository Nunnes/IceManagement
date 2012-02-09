#!/usr/bin/env python

class TransactionDTO:
	''' Clients' transactions and debts ''' 
	
	def __init__(self, clientName, quantity, price, credit = False):
		'''transaction data transfer objet'''
		self.quantity = quantity
		self.price = price
		self.credit = credit
                self.clientName = clientName
