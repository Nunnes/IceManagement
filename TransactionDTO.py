#!/usr/bin/env python

class TransactionDTO:
	''' Clients' transactions and debts ''' 
	
	def __init__(self, clientName, quantity, price, fiado = False):
		'''transaction data transfer objet'''
		self.quantity = quantity
		self.price = price
		self.fiado = fiado
                self.clientName = clientName
