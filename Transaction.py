#!/usr/bin/env python

class Transaction:
	''' Clients' transactions and debts ''' 
	
	def __init__(self, quantity, price, fiado = False):
		'''Initializes the transaction'''
		self.quantity = quantity
		self.price = price
		self.fiado = fiado