#!/usr/bin/env python

class Client:
	'''Represents a Client.'''
	population = 0
	

	def __init__(self, name,):
		'''Initializes the person's data.'''
		self.name = name
		print '(Initializing %s)' % self.name
		self.transactionList = [] 
		# When this client is created, he/she
		# adds to the population
		Client.population += 1

	def setName(self, name):
		self.name = name

	def getName(self,name):
		return self.name

	def delete(self):
		'''I am dying.'''

		if Client.population == 0:
			print 'Nao existem clientes registados.'
		else:
			print 'Encontram-se %d Clientes registados.' % Client.population
	
		print '%s says bye.' % self.name
		Client.population -= 1

	
	def howMany(self):
		'''Imprime o numero de Clientes'''
		if Client.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Client.population

	def buyIce(self):
		quant = input(' Quantity:  ')
		price = input('Price: ')
		optional = raw_input('Fiado s/N: ')
		
		fiado = False

		if optional == "s":
			fiado = True
		if optional == "n":
			fiado = False

		self.transactionList.append(Transaction(quant, price, fiado))		

class Transaction:
	''' Clients' transactions and debts ''' 
	
	def __init__(self, quantity, price, fiado = False):
		'''Initializes the transaction'''
		self.quantity = quantity
		self.price = price
		self.fiado = fiado